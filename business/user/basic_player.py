from business.user.abstract_player import Player
from business.character.character import Character
class BasicPlayer(Player):

    def __init__(self, fisrtname:str, lastname:str, username:str, age:int = None) -> None:
        super().__init__(fisrtname, lastname, age, username, 'basic-player')
        self.characters = []
    
    def add_character(self, character: Character) -> None:
        self.characters.append(character)

    def rm_character(self, name : str) -> None:
        for i, o in enumerate(self.characters):
            if o.name == name:
                del self.characters[i]
                break
    
    @staticmethod
    def load(username:str):
        import dao.player_dao as d
        basic_player = d.PlayerDao().load_basic_player(username)
        if basic_player:
            return basic_player