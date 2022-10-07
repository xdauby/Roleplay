from business.user.abstract_user import User

class Organiser(User):
    
    def __init__(self, fisrtname: str, lastname: str, age:int, id : int = None) -> None:
        super().__init__(fisrtname, lastname, age)
        self.id = id

    def load_all_tables(self):
        pass
    
    @staticmethod
    def load(username:str):
        pass
    