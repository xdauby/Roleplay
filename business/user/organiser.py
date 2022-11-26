from business.user.abstract_user import User
from business.notification.notification import Notification

class Organiser(User):
    """Organiser Class

    Args:
        User
    """    
    
    def __init__(self, firstname: str
                        , lastname: str
                        , username:str
                        , age:int
                        , id : int = None
                        , password:str='') -> None:
        """init

        Args:
            firstname (str): firstname of the Organiser
            lastname (str): lastname of the Organiser
            username (str): username of the Organiser
            age (int): age of the Organiser
            id (int, optional): id of the Organiser. Defaults to None.
            password (str, optional): password of the Organiser. Defaults to ''.
        """        
        super().__init__(firstname=firstname
                        , lastname=lastname
                        , username=username
                        , password=password
                        , age=age)

    def notify_player(self, notif: str, username: str) -> bool:
        """notify a player

        Args:
            notif (str): message to the player
            username (str): player concerned of the notification

        Returns:
            bool: True if the notification has been added, else False 
        """        
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
        """load Organiser

        Args:
            username (str): username of the Organiser to load

        Returns:
            Organiser: loaded Organiser
        """        
        
        from dao.organiser_dao import OrganiserDao
        organiser = OrganiserDao().load(username)
        return organiser

