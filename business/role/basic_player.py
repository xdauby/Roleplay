from business.character.character import Character

class BasicPlayer:

    def __init__(self, username:str ) -> None:

        self.username = username
        self.characters = []
        
    def add_character(self, character: Character) -> bool:
        
        if len(self.characters) < 3:
            from dao.basic_player_dao import BasicPlayerDao
            created = BasicPlayerDao().add_character(character)
            if created:
                self.characters.append(character)
                return True
        return False


    def rm_character(self, id:int) -> bool:
        
        for character in self.characters:
            if character.id == id:
                from dao.basic_player_dao import BasicPlayerDao
                if BasicPlayerDao().rm_character(id):
                    self.characters.remove(character)
                    return True
        return False
    
    @staticmethod
    def load(username:str):
        from dao.basic_player_dao import BasicPlayerDao
        return BasicPlayerDao().load(username)

    def __str__(self):
        
        string = ''
        for character in self.characters:
            string += character.__str__() + " "
        
        overall = f' Username associated : {self.username},\n {string}' 
        return overall


    def __eq__(self, obj):
        if isinstance(obj,BasicPlayer):
            if self.username == obj.username and self.characters == obj.characters and self.tables_id == obj.tables_id:
                return True
        return False