from curses import halfdelay
from typing import List, Optional
from dao.basic_player_dao import BasicPlayerDao
from dao.db_connection import DBConnection

from business.scenario.scenario import Scenario
from business.character.character import Character
from business.user.game_master import GameMaster
from business.user.basic_player import BasicPlayer
from business.table.table import Table
from business.user.abstract_player import Player

class TableDao:

    def load(self, id:int):
        
        table = None

        
        request_gamemaster = "SELECT DISTINCT * FROM game "\
                            "LEFT JOIN scenario on scenario.id_scenario = game.id_scenario "\
                            "LEFT JOIN player on scenario.username = player.username "\
                            "where game.id_game = %(id)s;"
        
        request_basicplayer = "SELECT * FROM game "\
                                "LEFT JOIN char_reg_game on game.id_game = char_reg_game.id_game "\
                                "inner JOIN character on character.id_char = char_reg_game.id_char "\
                                "inner JOIN player on character.username = player.username "\
                                "where game.id_game = %(id)s;"

        requests = [request_gamemaster,request_basicplayer]
        res = []
       
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                for reqs in requests:
                    cursor.execute(
                        reqs
                    , {'id':id})
                    res.append(cursor.fetchall())

        res_gamemaster = res[0]
        res_basicplayer = res[1]

        if res_gamemaster or res_basicplayer:
            
            #if the table is empty
            if not res_gamemaster[0]['id_scenario']:
                table = Table(half_day=res_gamemaster[0]['halfday'],active=res_gamemaster[0]['active'],id=res_gamemaster[0]['id_game'])
                return table
            
            else:
                for rows in res_gamemaster:
                    scenario = Scenario(name=rows['name'], 
                                        description=rows['description'], 
                                        id = rows['id_scenario'], 
                                        username=rows['username'])
                    
                    game_master = GameMaster(rows['firstname']
                                            , rows['lastname']
                                            , rows['username'])
                    game_master.scenarios.append(scenario)

                    player = Player(firstname=rows['firstname'], 
                                    lastname=rows['lastname'], 
                                    username=rows['username'], 
                                    age=rows['age'], 
                                    game_master=game_master)

                    table = Table(half_day=rows['halfday']
                                , active=rows['active']
                                , id=rows['id_game'])
                    
                    table.players.append(player)
                    table.scenario = scenario
        
                for rows in res_basicplayer:
                    character = Character(name=rows['name']
                                        , level=rows['level']
                                        , id = rows['id_char']
                                        , equipment = rows['equipment']
                                        , race = rows['race']
                                        , skill = rows['skill']
                                        , username=rows['username'])
                    
                    basic_player = BasicPlayer(rows['firstname'], rows['lastname'], rows['username'])
                    basic_player.characters.append(character)
                    
                    player = Player(firstname=rows['firstname'], 
                                    lastname=rows['lastname'], 
                                    username=rows['username'], 
                                    age=rows['age'], 
                                    basic_player=basic_player)
                    
                    table.players.append(player)
                    table.characters.append(character)
                    
        return table

    def load_user_tables(self, table_id):
        tables = []
        request_gamemaster = "SELECT * FROM game "\
                            "inner JOIN scenario on scenario.id_scenario = game.id_scenario "\
                            "inner JOIN player on scenario.username = player.username "\
                            "where game.id_game IN %s;"
        
        request_basicplayer = "SELECT * FROM game "\
                                "LEFT JOIN char_reg_game on game.id_game = char_reg_game.id_game "\
                                "inner JOIN character on character.id_char = char_reg_game.id_char "\
                                "inner JOIN player on character.username = player.username "\
                                "where game.id_game IN %s;"

        requests = [request_gamemaster,request_basicplayer]
        res = []
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                for reqs in requests:
                    cursor.execute(
                        reqs
                    , (tuple(table_id),))
                    res.append(cursor.fetchall())

        res_gamemaster = res[0]
        res_basicplayer = res[1]

        if res_gamemaster:
            for rows in res_gamemaster:
                scenario = Scenario(name=rows['name'], 
                                        description=rows['description'], 
                                        id = rows['id_scenario'], 
                                        username=rows['username'])
                    
                game_master = GameMaster(rows['firstname']
                                            , rows['lastname']
                                            , rows['username'])
                game_master.scenarios.append(scenario)

                player = Player(firstname=rows['firstname'], 
                                    lastname=rows['lastname'], 
                                    username=rows['username'], 
                                    age=rows['age'], 
                                    game_master=game_master)

                table = Table(half_day=rows['halfday']
                                , active=rows['active']
                                , id=rows['id_game'])
                    
                table.players.append(player)
                table.scenario = scenario
                tables.append(table)
    
        if res_basicplayer:
            for table in tables:
                for rows in res_basicplayer:
                    if rows['id_game'] == table.id:
                        character = Character(name=rows['name']
                                        , level=rows['level']
                                        , id = rows['id_char']
                                        , equipment = rows['equipment']
                                        , race = rows['race']
                                        , skill = rows['skill']
                                        , username=rows['username'])
                    
                        basic_player = BasicPlayer(rows['firstname'], rows['lastname'], rows['username'])
                        basic_player.characters.append(character)
                    
                        player = Player(firstname=rows['firstname'], 
                                    lastname=rows['lastname'], 
                                    username=rows['username'], 
                                    age=rows['age'], 
                                    basic_player=basic_player)
                    
                        table.players.append(player)
                        table.characters.append(character)
                
        return tables


    def add_gm_to_table(self, id_scenario: int, id_game: int) -> bool:

        updated = False

        request = 'UPDATE game SET id_scenario=%(id_scenario)s '\
                    'WHERE id_game = %(id_game)s and active = TRUE;'\

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request, 
                        {'id_scenario': id_scenario,
                         'id_game': id_game})                        
                if cursor.rowcount :
                    updated = True

        return updated        

    def add_bp_to_table(self, id_character:int, id_game: int) -> bool:

        updated = False

        request = 'INSERT INTO char_reg_game(id_game, id_char) VALUES'\
                  '(%(id_game)s,%(id_character)s);'

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request, 
                        {'id_character': id_character,
                         'id_game': id_game}) 
                if cursor.rowcount :
                    updated = True

        return updated        

    def rm_gm_from_table(self, id_game:int) -> bool:

        removed = False

        request = 'UPDATE game SET id_scenario=NULL '\
                  'WHERE id_game = %(id_game)s;'

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request, 
                        {'id_game': id_game}) 
                if cursor.rowcount :
                    removed = True

        return removed 

    def rm_bp_from_table(self, id_game:int, id_character:int) -> bool:

        removed = False

        request = 'DELETE FROM char_reg_game '\
                  'WHERE id_game = %(id_game)s AND id_char = %(id_character)s;'
    

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request, 
                        {'id_game': id_game,
                        'id_character': id_character}) 
                if cursor.rowcount :
                    removed = True

        return removed 

    def active_table(self, id_game:int) -> bool:

        active = False
        request = 'UPDATE game SET active=TRUE '\
                  'WHERE id_game = %(id_game)s; '

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request, 
                        {'id_game': id_game}) 
                if cursor.rowcount :
                    active = True

        return active

    def desactive_table(self, id_game:int) -> bool:

        desactive = False
        request = 'UPDATE game SET active=FALSE '\
                  'WHERE id_game = %(id_game)s; '

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request, 
                        {'id_game': id_game}) 
                if cursor.rowcount :
                    desactive = True

        return desactive


    def load_all(self, show_desactive:bool):
        
        if show_desactive:
            request_gamemaster = "SELECT * FROM game "\
                                "LEFT JOIN scenario on scenario.id_scenario = game.id_scenario "\
                                "LEFT JOIN player on scenario.username = player.username "\
                                "ORDER BY id_game;"
        else:
            request_gamemaster = "SELECT * FROM game "\
                                "LEFT JOIN scenario on scenario.id_scenario = game.id_scenario "\
                                "LEFT JOIN player on scenario.username = player.username "\
                                "WHERE active = TRUE "\
                                "ORDER BY id_game;"

        
        request_basicplayer = "SELECT * FROM game "\
                                "LEFT JOIN char_reg_game on game.id_game = char_reg_game.id_game "\
                                "inner JOIN character on character.id_char = char_reg_game.id_char "\
                                "inner JOIN player on character.username = player.username;"

        requests = [request_gamemaster,request_basicplayer]
        res = []
        
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                for reqs in requests:
                    cursor.execute(
                        reqs
                    )
                    res.append(cursor.fetchall())

        res_gamemaster = res[0]
        res_basicplayer = res[1]
        tables = []

        if res_gamemaster:
            for rows in res_gamemaster:
                if rows['id_scenario']:
                    
                    scenario = Scenario(name=rows['name'], 
                                            description=rows['description'], 
                                            id = rows['id_scenario'], 
                                            username=rows['username'])
                        
                    game_master = GameMaster(rows['firstname']
                                                , rows['lastname']
                                                , rows['username'])
                    game_master.scenarios.append(scenario)

                    player = Player(firstname=rows['firstname'], 
                                        lastname=rows['lastname'], 
                                        username=rows['username'], 
                                        age=rows['age'], 
                                        game_master=game_master)

                    table = Table(half_day=rows['halfday']
                                    , active=rows['active']
                                    , id=rows['id_game'])
                        
                    table.players.append(player)
                    table.scenario = scenario
                    tables.append(table)
                    
                else:
                    table = Table(half_day=rows['halfday'],active=rows['active'],id=rows['id_game'])
                    tables.append(table)

    
        if res_basicplayer:
            for table in tables:
                for rows in res_basicplayer:
                    if rows['id_game'] == table.id:

                        character = Character(name=rows['name']
                                        , level=rows['level']
                                        , id = rows['id_char']
                                        , equipment = rows['equipment']
                                        , race = rows['race']
                                        , skill = rows['skill']
                                        , username=rows['username'])
                    
                        basic_player = BasicPlayer(rows['firstname'], rows['lastname'], rows['username'])
                        basic_player.characters.append(character)
                    
                        player = Player(firstname=rows['firstname'], 
                                    lastname=rows['lastname'], 
                                    username=rows['username'], 
                                    age=rows['age'], 
                                    basic_player=basic_player)
                    
                        table.players.append(player)
                        table.characters.append(character)

        
        return tables


