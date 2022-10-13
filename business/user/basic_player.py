from business.user.abstract_player import Player
from business.character.character import Character

class BasicPlayer(Player):

    def __init__(self, fisrtname:str, lastname:str, username:str, age:int = None) -> None:
        super().__init__(fisrtname, lastname, age, username, 'basic-player')
        self.characters = []
        self.tables_id = []
        self.tables = []
        
    def add_character(self, character: Character) -> bool:
        
        if len(self.characters) < 3:
            from dao.character_dao import CharacterDao
            created = CharacterDao().add(character)
            if created:
                self.characters.append(character)
                return True
        return False


    def rm_character(self, id:int) -> bool:
        
        for i, o in enumerate(self.characters):
            if o.id == id:
                from dao.character_dao import CharacterDao
                if CharacterDao().rm(id):
                    del self.characters[i]
                    return True
        return False


    def load_player_tables(self) -> None:
        if self.tables_id:
            from dao.table_dao import TableDao
            self.tables = TableDao().load_user_tables(self.tables_id)
    
    @staticmethod
    def load(username:str):
        from dao.basic_player_dao import BasicPlayerDao
        basic_player = BasicPlayerDao().load(username)
        if basic_player:
            return basic_player