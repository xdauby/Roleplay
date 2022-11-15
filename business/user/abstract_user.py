from abc import ABC, abstractmethod

class User(ABC):

    def __init__(self, firstname: str,
                lastname: str, 
                username:int,
                password:str, 
                age:int = None):
        
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.age = age
        self.password = password


    @staticmethod
    def load(username:str):
        pass