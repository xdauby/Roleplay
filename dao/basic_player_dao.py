from typing import List, Optional
from dao.db_connection import DBConnection

from business.character.character import Character
from business.user.basic_player import BasicPlayer



class BasicPlayerDao:

    def add(self) -> bool:
        pass

    def rm(self) -> bool:
        pass

    def load(self, username:str):
        
        basic_player = None

        char_request = "SELECT * FROM player  "\
                    "LEFT JOIN character ON character.username =  player.username "\
                    "WHERE player.username =  %(username)s;"          
        table_id_request = "SELECT DISTINCT game.id_game FROM character "\
                            "LEFT JOIN char_reg_game on character.id_char =  char_reg_game.id_char "\
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
        

        if res: 
            if res[0][0]['id_char']: #no id set to 0, test if is not None 
                basic_player = BasicPlayer(res[0][0]['firstname'], res[0][0]['lastname'], res[0][0]['username'])
                for rows in res[0]:
                    character = Character(name=rows['name']
                                      , level=rows['level']
                                      , id = rows['id_char']
                                      , equipment = rows['equipment']
                                      , race = rows['race']
                                      , skill = rows['skill'])
                    
                    basic_player.characters.append(character)
                for table_id in res[1]:
                    if table_id['id_game']:
                        basic_player.tables_id.append(table_id['id_game'])
            else:
                basic_player = BasicPlayer(res[0][0]['firstname'], res[0][0]['lastname'], res[0][0]['username'])
        return basic_player
        

    def load_all(self):
        pass

