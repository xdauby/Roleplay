from typing import List, Optional
from business.user.basic_player import BasicPlayer
from dao.db_connection import DBConnection
from dao.abstract_dao import Dao
from dao.character_dao import CharacterDao

class BasicPlayerDao(Dao):

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
            basic_player = BasicPlayer(res['firstname'], res['lastname'], res['username'])
            basic_player_characters = CharacterDao().load_user_char(username)
            basic_player.characters = basic_player_characters
        
        return basic_player

    def load_all(self):
        pass

    


