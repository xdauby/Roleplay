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
        
        bp_res = res[0]
        table_id_res = res[1]        

        if bp_res: 
            if bp_res[0]['id_char']: #no id set to 0, test if is not None 
                basic_player = BasicPlayer(bp_res[0]['firstname'], bp_res[0]['lastname'], bp_res[0]['username'])
                for rows in bp_res:
                    character = Character(name=rows['name']
                                      , level=rows['level']
                                      , id = rows['id_char']
                                      , equipment = rows['equipment']
                                      , race = rows['race']
                                      , skill = rows['skill'])
                    
                    basic_player.characters.append(character)
                for table_id in table_id_res:
                    if table_id['id_game']:
                        basic_player.tables_id.append(table_id['id_game'])
            else:
                basic_player = BasicPlayer(bp_res[0]['firstname'], bp_res[0]['lastname'], bp_res[0]['username'])
        return basic_player
        

    def load_all(self):
        pass

