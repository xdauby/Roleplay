from business.user.abstract_user import User
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
            if isinstance(obj,Organiser):
                if self.firstname == obj.firstname and self.lastname == obj.lastname and self.username == obj.username and self.age == obj.age and self.password == obj.password:
                    return True
            return False

    @staticmethod
    def load(username:str):
        
        from dao.organiser_dao import OrganiserDao
        organiser = OrganiserDao().load(username)
        return organiser

