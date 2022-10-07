from business.user.abstract_user import User
from business.user.abstract_player import Player
from business.user.basic_player import BasicPlayer
from business.user.game_master import GameMaster

class PlayerFactory:

    def instantiate_player(self, user_type: str, firstname:str, lastname: str, username: str, age: int = None) -> Player:
        
        player = None

        if user_type=='game-master':
            player = GameMaster(fisrtname=firstname, lastname=lastname, username=username, age=age)
        elif user_type=='basic-player':
            player = BasicPlayer(fisrtname=firstname, lastname=lastname, username=username, age=age)

        return player