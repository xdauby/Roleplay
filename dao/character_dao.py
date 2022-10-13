from typing import List, Optional
from dao.db_connection import DBConnection
from dao.abstract_dao import Dao
from business.character.character import Character


class CharacterDao(Dao):

    def add(self, character: Character) -> bool:

        created = False
        request = "INSERT INTO character(username, name, level, equipment, equipment_desc, race, race_desc, skill, skill_desc) VALUES "\
                  "(%(username)s,%(name)s, %(level)s, %(equipment)s, %(equipment_desc)s, %(race)s, %(race_desc)s, %(skill)s, %(skill_desc)s)"\
                  "RETURNING id_char;"
        
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request
                , {"username" : character.belong_to
                  ,"name" : character.name
                  ,"level" : character.level
                  ,"equipment" : character.equipment
                  ,"equipment_desc" : character.equipment_desc
                  ,"race" : character.race
                  ,"race_desc": character.race_desc
                  ,"skill" : character.skill
                  ,"skill_desc" : character.skill_desc})
                res = cursor.fetchone()
        if res:
            character.id = res['id_char']
            created = True

        return created
        

    def rm(self, id:int) -> bool:
        
        removed = False
        request = "DELETE FROM character WHERE id_char = %(id)s;"\
                  "SELECT COUNT(*) FROM character WHERE id_char = %(id)s;"
        
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request
                , {"id" : id})
                res = cursor.fetchone()
        if not res['count']:
            removed = True

        return removed

    def load(self, id:int):

        character = []
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

        characters = []
        request = "SELECT * FROM character WHERE username=%(username)s"
        
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request
                , {"username" : username})
                res = cursor.fetchall()

        if res:
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
