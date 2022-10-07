from business.user.abstract_user import User

class Player(User):
    
    def __init__(self, fisrtname: str, lastname: str, age: int, username: str, type_player: str = None):
        super().__init__(fisrtname, lastname, age)
        self.username = username
        self.type_player = type_player
    