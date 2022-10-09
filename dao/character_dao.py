from typing import List, Optional
from dao.db_connection import DBConnection
from dao.abstract_dao import Dao
from business.character.character import Character


class CharacterDao(Dao):

    def add(self) -> bool:
        pass

    def rm(self) -> bool:
        pass

    def load(self, id:int):

        character = None
        request = "SELECT * FROM Character WHERE id_char=%(id)s"
        
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request
                , {"id" : id})
                res = cursor.fetchone()

        if res:
            character = Character(name=res['name']
                                  , level=res['level']
                                  , id = res['id_char']
                                  , equipment = res['equipment']
                                  , race = res['race']
                                  , skill = res['skill'])
        return character

    def load_user_char(self, username:str):

        characters = None
        request = "SELECT * FROM character WHERE username=%(username)s"
        
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request
                , {"username" : username})
                res = cursor.fetchall()

        if res:
            characters = []
            for row in res:
                curr_char = Character(name=row['name']
                                      , level=row['level']
                                      , id = row['id_char']
                                      , equipment = row['equipment']
                                      , race = row['race']
                                      , skill = row['skill'])
                characters.append(curr_char)
        return characters

    def load_all(self):
        pass
