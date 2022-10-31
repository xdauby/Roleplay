from abc import ABC, abstractmethod

class User(ABC):

    def __init__(self, fisrtname: str,
                lastname: str, 
                username:int,
                password:str, 
                age:int = None):
        
        self.firstname = fisrtname
        self.lastname = lastname
        self.username = username
        self.age = age
        self.password = password

    @abstractmethod
    def load_all_tables():
        pass

    @staticmethod
    def load(username:str):
        pass