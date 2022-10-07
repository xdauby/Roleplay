from typing import List, Optional
from utils_.singleton import Singleton
from business.user.basic_player import BasicPlayer
from dao.db_connection import DBConnection

class PlayerDao(metaclass = Singleton):

    def add(self) -> bool:
        pass

    def rm(self) -> bool:
        pass

    def load(self, username:str):
        
        #ceci est un test

        basic_player = None
        request = "SELECT * FROM PLAYER WHERE username=%(username)s"
        
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request
                , {"username" : username})
                res = cursor.fetchone()

        if res:        
            basic_player = BasicPlayer(res['first_name'], res['last_name'], res['username'])
        
        return basic_player

    def load_all(self):
        pass

    


