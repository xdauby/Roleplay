from typing import List, Optional
from dao.basic_player_dao import BasicPlayerDao
from dao.db_connection import DBConnection

from business.scenario.scenario import Scenario
from business.character.character import Character
from business.role.game_master import GameMaster
from business.role.basic_player import BasicPlayer
from business.table.table import Table
from business.user.player import Player
from dao.player_dao import PlayerDao

class TableDao:
    """Table Dao class
    """    

    def load(self, id:int) -> Table:
        """load Table from database

        Args:
            id (int): id of the table to load

        Returns:
            Table: loaded Table
        """        
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
                table = Table(half_day=res_gamemaster[0]['halfday']
                                , active=res_gamemaster[0]['active']
                                , id=res_gamemaster[0]['id_game'])
                return table
            
            else:
                for rows in res_gamemaster:

                    
                    scenario = Scenario(name=rows['name'], 
                                        description=rows['description'], 
                                        id = rows['id_scenario'], 
                                        username=rows['username'])
                
                    player = PlayerDao().load(rows['username'])

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
                    
                    player = PlayerDao().load(rows['username'])
                    table.players.append(player)
                    table.characters.append(character)
                    
        return table

    def add_gm_to_table(self, id_scenario: int, id_game: int) -> bool:
        """add a Player with a Scenario in a table, in database

        Args:
            id_scenario (int): id Scenario of the Player
            id_game (int): id of the table

        Returns:
            bool: True if the The player has been added to the table in database, else False
        """        
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
        """add a Player with a Character in a table, in database

        Args:
            id_character (int): id of the Character of the Player to add
            id_game (int): id of the table

        Returns:
            bool: True if the The player has been added to the table in database, else False
        """        
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
        """remove Player with a Scenario from the table, in database

        Args:
            id_game (int): table id

        Returns:
            bool: True if the Player has been removed from the table in db, else False
        """        
        removed = False

        request = 'DELETE FROM char_reg_game WHERE id_game = %(id_game)s;'\
                  'UPDATE game SET id_scenario=NULL '\
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
        """remove BasicPlayer with a Character from the table, in database

        Args:
            id_game (int): table id

        Returns:
            bool: True if the Player has been removed from the table in db, else False
        """  
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
        """active a Table in database

        Args:
            id_game (int): id of the table to active

        Returns:
            bool: True if the Table has been activated, else False
        """
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
        """desactive a Table in database

        Args:
            id_game (int): id of the table to desactivate

        Returns:
            bool: True if the table has been desactivated in db, else False
        """
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

    def load_user_tables(self, table_id):
        """Load a list of Table from a list of id Tables. The player in those tables are partially loaded,
           because it's just used for display. Please do not use Table methods in thoses Tables.

        Args:
            table_id (list(int)): list of table id to load

        Returns:
            list(Table) : list of Tables loaded
        """ 
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
                    
                game_master = GameMaster(username=rows['username'])
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
                    
                        basic_player = BasicPlayer(username=rows['username'])
                        basic_player.characters.append(character)
                    
                        player = Player(firstname=rows['firstname'], 
                                    lastname=rows['lastname'], 
                                    username=rows['username'], 
                                    age=rows['age'], 
                                    basic_player=basic_player)
                    
                        table.players.append(player)
                        table.characters.append(character)
                
        return tables



    def load_all(self, show_desactive:bool):
        """Load all Tables. The player in those tables are partially loaded,
           because it's just used for display. Please do not use Table methods in thoses Tables.

        Args:
            show_desactive (bool): True to load all tables even desactivated ones, False for only activated Tables

        Returns:
            list(Table) : list of Tables to display
        """ 
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
                        
                    game_master = GameMaster(username=rows['username'])
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
                    table = Table(half_day=rows['halfday']
                                , active=rows['active']
                                , id=rows['id_game'])

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
                    
                        basic_player = BasicPlayer(username=rows['username'])
                        basic_player.characters.append(character)
                    
                        player = Player(firstname=rows['firstname'], 
                                    lastname=rows['lastname'], 
                                    username=rows['username'], 
                                    age=rows['age'], 
                                    basic_player=basic_player)
                    
                        table.players.append(player)
                        table.characters.append(character)

        
        return tables
