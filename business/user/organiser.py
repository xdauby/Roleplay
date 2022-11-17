from business.user.abstract_user import User
from business.role.game_master import GameMaster
from business.role.basic_player import BasicPlayer
from business.user.player import Player
from business.table.table import Table
from business.notification.notification import Notification

class Organiser(User):
    
    def __init__(self, firstname: str
                        , lastname: str
                        , username:str
                        , age:int
                        , id : int = None
                        , password:str='') -> None:

        super().__init__(firstname=firstname
                        , lastname=lastname
                        , username=username
                        , password=password
                        , age=age)

    def notify_player(self, notif: str, username: str) -> bool:

        notif_player = Notification(notification=notif, username=username)
        from dao.organiser_dao import OrganiserDao
        return OrganiserDao().save_notif(notif_player)

    def __eq__(self, obj) -> bool:
            if isinstance(obj,Player):
                if self.firstname == obj.firstname and self.lastname == obj.lastname and self.username == obj.username and self.age == obj.age:
                    return True
            return False

    @staticmethod
    def load(username:str):
        
        from dao.organiser_dao import OrganiserDao
        organiser = OrganiserDao().load(username)
        return organiser

