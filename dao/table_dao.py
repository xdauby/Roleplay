from typing import List, Optional
from dao.db_connection import DBConnection

from business.scenario.scenario import Scenario
from business.character.character import Character
from business.user.game_master import GameMaster
from business.user.basic_player import BasicPlayer
from business.table.table import Table

class TableDao:

    def add(self, table:Table) -> bool:
        pass

    def rm(self, id:int ) -> bool:
        pass

    def load(self, id:int):
        pass

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
                scenario = Scenario(name=rows['name'], description=rows['description'], id = rows['id_scenario'])
                game_master = GameMaster(rows['firstname'], rows['lastname'], rows['username'])
                game_master.scenarios.append(scenario)
                table = Table(half_day=rows['halfday'],id=rows['id_game'])
                table.game_master = game_master
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
                                      , skill = rows['skill'])
                        basic_player = BasicPlayer(rows['firstname'], rows['lastname'], rows['username'])
                        basic_player.characters.append(character)
                        table.basic_player.append(basic_player)
        
        return tables



    def load_all(self):
        request_gamemaster = "SELECT * FROM game "\
                            "inner JOIN scenario on scenario.id_scenario = game.id_scenario "\
                            "inner JOIN player on scenario.username = player.username;"
        
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
                scenario = Scenario(name=rows['name'], description=rows['description'], id = rows['id_scenario'])
                game_master = GameMaster(rows['firstname'], rows['lastname'], rows['username'])
                game_master.scenarios.append(scenario)
                table = Table(half_day=rows['halfday'],id=rows['id_game'])
                table.game_master = game_master
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
                                      , skill = rows['skill'])
                        basic_player = BasicPlayer(rows['firstname'], rows['lastname'], rows['username'])
                        basic_player.characters.append(character)
                        table.basic_player.append(basic_player)
        
        return tables
        

