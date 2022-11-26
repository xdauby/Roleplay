from utils_.singleton import Singleton
from business.user.player import Player
from business.user.organiser import Organiser

class Session(metaclass=Singleton):
    def __init__(self):
        
        self.username: str = None
        self.player: Player = None
        self.organiser: Organiser = None 
