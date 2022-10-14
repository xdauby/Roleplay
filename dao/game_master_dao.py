from typing import List, Optional
from dao.db_connection import DBConnection

from business.scenario.scenario import Scenario
from business.user.game_master import GameMaster



class GameMasterDao:

    
    def add(self) -> bool:
        pass

    def rm(self) -> bool:
        pass

    def load(self, username:str):

        game_master = None
        
        scen_request = "SELECT * FROM player "\
                    "LEFT JOIN scenario on player.username = scenario.username "\
                    "WHERE player.username = %(username)s;"
        
        table_id_request = "SELECT DISTINCT game.id_game FROM scenario "\
                            "LEFT JOIN game on game.id_scenario = scenario.id_scenario "\
                            "WHERE scenario.username = %(username)s; "
     
        requests = [scen_request,table_id_request]
        res = []

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                for reqs in requests:
                    cursor.execute(
                        reqs
                        , {"username" : username})
                    res.append(cursor.fetchall())
        
        gm_res = res[0]
        table_id_res = res[1]        


        if gm_res: 
            if gm_res[0]['id_scenario']: #no id set to 0, so we can do that
                game_master = GameMaster(gm_res[0]['firstname'], gm_res[0]['lastname'], gm_res[0]['username'])
                for rows in gm_res:
                    scenario = Scenario(rows['name'], rows['description'], id = rows['id_scenario'])
                    game_master.scenarios.append(scenario)
                for table_id in table_id_res:
                    if table_id['id_game']:
                        game_master.tables_id.append(table_id['id_game'])
            else:
                game_master = GameMaster(gm_res[0]['firstname'], gm_res[0]['lastname'], gm_res[0]['username'])
        return game_master
        
    
        

    def load_all(self):
        pass

