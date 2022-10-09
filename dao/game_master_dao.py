from typing import List, Optional
from dao.db_connection import DBConnection
from dao.abstract_dao import Dao
from dao.scenario_dao import ScenarioDao

from business.user.game_master import GameMaster



class GameMasterDao(Dao):

    
    def add(self) -> bool:
        pass

    def rm(self) -> bool:
        pass

    def load(self, username:str):

        #ceci est un test
        game_master = None
        request = "SELECT * FROM PLAYER WHERE username=%(username)s"
        
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request
                , {"username" : username})
                res = cursor.fetchone()

        if res:        
            game_master = GameMaster(res['firstname'], res['lastname'], res['username'])
            game_master_scenarios = ScenarioDao().load_user_scenarios(username)
            game_master.scenarios = game_master_scenarios
        
        return game_master


    def load_all(self):
        pass



