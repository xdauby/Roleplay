from typing import List, Optional
from dao.db_connection import DBConnection

from business.character.character import Character
from business.role.basic_player import BasicPlayer

class BasicPlayerDao:
    """Dao of BasicPlayer
    """    
    
    def add_character(self, character: Character) -> bool:
        """add a Character to the data base

        Args:
            character (Character): Character to add

        Returns:
            bool: True if the Character has been added, else False
        """        
        created = False
        request = "INSERT INTO character(username, name, level, equipment, race, skill) VALUES "\
                  "(%(username)s,%(name)s, %(level)s, %(equipment)s, %(race)s, %(skill)s)"\
                  "RETURNING id_char;"
        
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request
                , {"username" : character.username
                  ,"name" : character.name
                  ,"level" : character.level
                  ,"equipment" : character.equipment
                  ,"race" : character.race
                  ,"skill" : character.skill})
                res = cursor.fetchone()
        if res:
            character.id = res['id_char']
            created = True

        return created
        

    def rm_character(self, id:int) -> bool:
        """remove a Character from database

        Args:
            id (int): id of the Character to remove

        Returns:
            bool: True if the Character has been removed, else False
        """        
        removed = False
        request = "DELETE FROM char_reg_game WHERE id_char = %(id)s;"\
                  "DELETE FROM character WHERE id_char = %(id)s;"\
                  "SELECT COUNT(*) FROM char_reg_game WHERE id_char = %(id)s;"
        
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request
                , {"id" : id})
                res = cursor.fetchone()
        if not res['count']:
            removed = True

        return removed

    def load(self, username:str) -> BasicPlayer:
        """Load BasicPlayer profile

        Args:
            username (str): username of the BasicPlayer profile to load

        Returns:
            BasicPlayer: BasicPlayer profile loaded
        """        
        basic_player = None

        requests = "SELECT * FROM player  "\
                        "LEFT JOIN character ON character.username =  player.username "\
                        "WHERE player.username =  %(username)s;"          
       
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    requests
                    , {"username" : username})
                res = cursor.fetchall()
            
        if res:
            basic_player = BasicPlayer(username=username)     
            for rows in res:
                if rows['id_char']: #no id set to 0, test if is not None 
                    character = Character(name=rows['name']
                                      , level=rows['level']
                                      , id = rows['id_char']
                                      , equipment = rows['equipment']
                                      , race = rows['race']
                                      , skill = rows['skill']
                                      , username = rows['username'])   
                    basic_player.characters.append(character)
                
        return basic_player
        

