from typing import List, Optional
from dao.db_connection import DBConnection

from business.scenario.scenario import Scenario
from business.role.game_master import GameMaster

class GameMasterDao:

    """Dao of GameMaster
    """    

    def add_scenario(self, scenario:Scenario) -> bool:
        """add a Scenario to the database

        Args:
            scenario (Scenario): Scenario to add

        Returns:
            bool: True if the Scenario has been added, else False
        """        
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
        """remove a Scenario from database

        Args:
            id (int): id of the Scenario to delete

        Returns:
            bool: True if the Scenario has been deleted, else False
        """        
        removed = False
        #delete a scenario implies to delete all the player registered at the table(s) where was the scenario
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

    def load(self, username:str) -> GameMaster:
        """load GameMaster profile

        Args:
            username (str): username of the GameMaster profile to load

        Returns:
            GameMaster: loaded GameMaster
        """        
        game_master = None
        
        requests = "SELECT * FROM player "\
                    "LEFT JOIN scenario on player.username = scenario.username "\
                    "WHERE player.username = %(username)s;"
    
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    requests
                    , {"username" : username})
                res = cursor.fetchall()

        if res: 
            game_master = GameMaster(username=username)            
            for rows in res:
                if rows['id_scenario']:
                    scenario = Scenario(name = rows['name']
                                        , description=rows['description']
                                        , id = rows['id_scenario']
                                        , username=rows['username'])
                    game_master.scenarios.append(scenario)
      
        return game_master
        
