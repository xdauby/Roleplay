from typing import List, Optional
from dao.db_connection import DBConnection

from business.character.character import Character
from business.user.basic_player import BasicPlayer

class BasicPlayerDao:
    
    def add_character(self, character: Character) -> bool:

        created = False
        request = "INSERT INTO character(username, name, level, equipment, equipment_desc, race, race_desc, skill, skill_desc) VALUES "\
                  "(%(username)s,%(name)s, %(level)s, %(equipment)s, %(equipment_desc)s, %(race)s, %(race_desc)s, %(skill)s, %(skill_desc)s)"\
                  "RETURNING id_char;"
        
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request
                , {"username" : character.username
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
        

    def rm_character(self, id:int) -> bool:
        
        removed = False
        request = "DELETE FROM character WHERE id_char = %(id)s;"\
                  "DELETE FROM char_reg_game WHERE id_char = %(id)s;"\
                  "SELECT COUNT(*) FROM char_reg_game WHERE id_char = %(id)s;"\
        
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request
                , {"id" : id})
                res = cursor.fetchone()
                print(res)
        if not res['count']:
            removed = True

        return removed

    def load(self, username:str):
        
        basic_player = None

        char_request = "SELECT * FROM player  "\
                        "LEFT JOIN character ON character.username =  player.username "\
                        "WHERE player.username =  %(username)s;"          
        table_id_request = "SELECT DISTINCT game.id_game, character.id_char FROM character "\
                            "LEFT JOIN char_reg_game on char_reg_game.id_char = character.id_char "\
                            "LEFT JOIN game on game.id_game = char_reg_game.id_game "\
                            "WHERE character.username = %(username)s; "

        requests = [char_request,table_id_request]
        res = []
     
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                for reqs in requests:
                    cursor.execute(
                        reqs
                        , {"username" : username})
                    res.append(cursor.fetchall())
        
        bp_res = res[0]
        table_id_res = res[1]        

        if bp_res:
            basic_player = BasicPlayer(bp_res[0]['firstname'], bp_res[0]['lastname'], bp_res[0]['username'])     
            for rows in bp_res:
                
                if rows['id_char']: #no id set to 0, test if is not None 
                    character = Character(name=rows['name']
                                      , level=rows['level']
                                      , id = rows['id_char']
                                      , equipment = rows['equipment']
                                      , race = rows['race']
                                      , skill = rows['skill']
                                      , username = rows['username'])   
                    basic_player.characters.append(character)
                
                for table_id in table_id_res:
      
                    if table_id['id_game']:
                        basic_player.tables_id.append(table_id['id_game'])
                
        return basic_player
        

