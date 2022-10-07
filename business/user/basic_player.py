from business.user.abstract_player import Player
from business.character.character import Character

class BasicPlayer(Player):

    def __init__(self, fisrtname:str, lastname:str, username:str, age:int = None) -> None:
        super().__init__(fisrtname, lastname, age, username, 'basic-player')
        self.characters = []
    
    def add_character(self, character: Character) -> None:
        
        if len(self.characters) < 3:
            self.characters.append(character)

    def rm_character(self, name : str) -> None:
        for i, o in enumerate(self.characters):
            if o.name == name:
                del self.characters[i]
                break
    
    def load_char(self) -> None:
        pass

    def load_player_tables(self) -> None:
        pass

    def load_all_tables(self):
        pass
    
    @staticmethod
    def load(username:str):
        #test
        from dao.basic_player_dao import PlayerDao
        basic_player = PlayerDao().load(username)
        if basic_player:
            return basic_player