from abc import ABC, abstractmethod

class User(ABC):
    """Abstract User class
    """    

    def __init__(self, firstname: str,
                lastname: str, 
                username:int,
                password:str, 
                age:int):
        """init

        Args:
            firstname (str): firstname of the user
            lastname (str): lastname of the user
            username (int): username of the user
            password (str): password of the user
            age (int): age of the user
        """                
        
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.age = age
        self.password = password


    @staticmethod
    def load(username:str):
        """load specific User

        Args:
            username (str): User username
        """        
        pass