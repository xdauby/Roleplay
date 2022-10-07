from typing import List, Optional
from utils_.singleton import Singleton
from dao.db_connection import DBConnection

from business.user.game_master import GameMaster
from dao.abstract_dao import Dao

class GameMasterDao(Dao,Singleton):

    
    def add(self):
        pass

    def rm(self):
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
            game_master = GameMaster('game-master', res['first_name'], res['last_name'], res['username'])
        
        return game_master


    def load_all(self):
        pass



