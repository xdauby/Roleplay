from typing import List, Optional
from dao.db_connection import DBConnection

from business.scenario.scenario import Scenario
from business.user.game_master import GameMaster

class GameMasterDao:

    

    def add_scenario(self, scenario:Scenario) -> bool:

        created = False
        request = "INSERT INTO scenario(username, name, description) VALUES "\
                  "(%(username)s,%(name)s,%(description)s)"\
                  "RETURNING id_scenario;"
        
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request
                , {"username" : scenario.username
                  ,"name" : scenario.name
                  ,"description" : scenario.description })
                res = cursor.fetchone()
        if res:
            scenario.id = res['id_scenario']
            created = True

        return created

    def rm_scenario(self, id:int ) -> bool:
        
        removed = False
        request = "DELETE FROM char_reg_game WHERE id_char in (select id_char from game as g JOIN char_reg_game c on g.id_game=c.id_game WHERE g.id_scenario = %(id)s) and id_game in (select c.id_game from game as g JOIN char_reg_game c on g.id_game=c.id_game WHERE g.id_scenario = %(id)s);"\
                  'UPDATE game SET id_scenario=NULL '\
                  'WHERE id_scenario = %(id)s;'\
                  "DELETE FROM scenario WHERE id_scenario = %(id)s;"\
                  "SELECT COUNT(*) FROM scenario WHERE id_scenario = %(id)s;"
 
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request
                , {"id" : id})
                res = cursor.fetchone()
        if not res['count']:
            removed = True

        return removed

    def load(self, username:str):

        game_master = None
        
        scen_request = "SELECT * FROM player "\
                    "LEFT JOIN scenario on player.username = scenario.username "\
                    "WHERE player.username = %(username)s;"
        
        table_id_request = "SELECT DISTINCT game.id_game, game.id_scenario FROM scenario "\
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
            
            game_master = GameMaster(gm_res[0]['firstname'], gm_res[0]['lastname'], gm_res[0]['username'])
            
            for rows in gm_res:
                if rows['id_scenario']:
                    scenario = Scenario(rows['name'], rows['description'], id = rows['id_scenario'], username=rows['username'])
                    game_master.scenarios.append(scenario)
            
            for table_id in table_id_res:
                if table_id['id_game']:
                    game_master.tables_id.append(table_id['id_game'])
      
        return game_master
        
