from abc import ABC

class User(ABC):

    def __init__(self, fisrtname: str,
                 lastname: str, age:int = None):
        self.firstname = fisrtname
        self.lastname = lastname
        self.age = age
