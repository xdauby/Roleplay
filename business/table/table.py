
from typing import List, Optional


from business.user.game_master import GameMaster
from business.user.basic_player import BasicPlayer
from business.scenario.scenario import Scenario
from business.character.character import Character
from business.user.abstract_player import Player

class Table:

    def __init__(self, half_day:int,
                        active:bool ,
                        id:int = None, 
                        scenario: Scenario=None, 
                        characters=[], 
                        players=[]) -> None:
        
        self.id = id
        self.half_day = half_day
        self.active = active
        
        self.scenario = scenario
        self.characters = []
        self.players = players
        

    def add_gamemaster(self, player: Player, id_scenario:int) -> bool:
        
        from dao.table_dao import TableDao
        #check if there is no game master and the table is ative
        if not(self.scenario) and self.active:
        
            #check if the player is already registered at a table for the same half day 
            if self.half_day in player.halfday:
                return False
            
            #check if the game master really have the scenario he try to register with
        
            elif TableDao().add_gm_to_table(id_scenario=id_scenario, id_game=self.id):
                for scenario in game_master.scenarios:
                    if scenario.id == id_scenario:
                        player.game_master.tables_id.append(self.id)
                        player.tables.append(self.id)
                        player.halfday.append(self.half_day)
                        self.scenario = scenario
                        self.players.append(player)
                        return True
        return False

    def add_basicplayer(self, player: Player, id_character:int)-> bool:

        #check if there is a game master and the table is ative
        if self.scenario and self.active:

            #check if the basic player can join the table
            if len(self.characters) < 4: 
                
                #check if the player is already registered at a table for the same half day 
                if self.half_day in player.halfday:
                    return False

                #check if the player really have the character he try to register with
                from dao.table_dao import TableDao
                if TableDao().add_bp_to_table(id_character=id_character, id_game=self.id):
                    for character in basic_player.characters:
                        if character.id == id_character:
                            player.basic_player.tables_id.append(self.id)
                            player.tables.append(self.id)
                            player.halfday.append(self.half_day)
                            self.characters.append(character)
                            self.players.append(player)
                            return True
        return False

    

    def rm_player(self, username:str) -> bool:
        
        removed = False
        #if a gamemaster is removed, all the players arround the the table are removed
        if self.scenario.username == username:
            #remove from db
            from dao.table_dao import TableDao
            TableDao().rm_gm_from_table(self.id)
            #remove from itself
            self.scenario = None
            self.characters = []
            self.players = []         
            removed = True
            #maybe delete from player ...
            return removed

        #if we delete a basic_player
        if self.characters:
            #get his character
            for character in self.characters:
                if character.username == username:
                    #delete the character from the table
                    from dao.table_dao import TableDao
                    TableDao().rm_bp_from_table(self.id, character.id)
                    self.characters.remove(character)
                    #delete the player from the table
                    for player in self.players:
                        if player.username == username:
                            self.players.remove(player)
                            removed = True
                            return removed
    
        return removed
    
    @staticmethod
    def load(table_id : int):
        from dao.table_dao import TableDao
        return TableDao().load(table_id)
    
    def active_table(self) -> bool:

        from dao.table_dao import TableDao
        if TableDao().active_table(self.id):
            self.active = True
            return True
        return False 

    def desactive_table(self) -> bool:

        from dao.table_dao import TableDao
        if self.scenario:
            username_gm = self.scenario.username
            self.rm_player(username_gm)
        if TableDao().desactive_table(self.id):
            self.active = False
            return True
        return False


    def __str__(self) -> str:

        

        bp_str = ''

        for character in self.characters:
            bp_str += f'{character.username} with Character {character.name} \n'

        if self.scenario:
            view = f'\nTable id : {self.id}, half day : {self.half_day}, acivate : {self.active} \n Game Master : {self.scenario.username} with Scenario {self.scenario.name}\n' + bp_str
        else:
            view = f'Table id : {self.id}, half day : {self.half_day}, acivate : {self.active}, table empty.'
        
        return view
        

