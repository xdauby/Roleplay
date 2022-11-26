from business.user.abstract_user import User
from business.role.game_master import GameMaster
from business.role.basic_player import BasicPlayer
from business.notification.notification import Notification

class Player(User):
    """Player class

    Args:
        User
    """    
    
    def __init__(self, firstname: str
                        , lastname: str
                        , username: str
                        , age: int
                        , game_master: GameMaster=None
                        , basic_player: BasicPlayer=None
                        , notification: Notification=None
                        , password:str=''):
        """init

        Args:
            firstname (str): firstname of the Player
            lastname (str): lastname of the Player
            username (str): username of the Player
            age (int): age of the Player
            game_master (GameMaster, optional): game_master profile of the Player. Defaults to None.
            basic_player (BasicPlayer, optional): basic_player profile of the Player. Defaults to None.
            notification (Notification, optional): notification of the Player. Defaults to None.
            password (str, optional): password of the Player. Defaults to ''.
        """        
        super().__init__(firstname=firstname
                        , lastname=lastname
                        , username=username
                        , password=password
                        , age=age)
   
        self.tables = []
        self.halfday = []
        self.basic_player = basic_player
        self.game_master = game_master
        self.notification = notification
    
    def delete_notif(self) -> None:
        """delete Player notification
        """        
        from dao.player_dao import PlayerDao
        if PlayerDao().delete_notif(self.username):
            self.notification = None

    def save(self) -> bool:
        """save Player in data base,
           Only User attributes are save.

        Returns:
            bool: True if the Player has been saved, else false
        """         
        from dao.player_dao import PlayerDao
        return PlayerDao().save(self)

    def __eq__(self, obj) -> bool:
            if isinstance(obj,Player):
                if self.tables == obj.tables and self.halfday == obj.halfday and self.basic_player == obj.basic_player and self.game_master == obj.game_master and self.firstname == obj.firstname and self.lastname == obj.lastname and self.username == obj.username and self.age == obj.age and self.password == obj.password and self.notification == obj.notification:
                    return True
            return False

    @staticmethod
    def load(username:str):
        """load Player

        Args:
            username (str): username of the Player to load

        Returns:
            Player: loaded Player
        """        
        from dao.player_dao import PlayerDao
        return PlayerDao().load(username)

    @staticmethod
    def delete(username:str) -> bool:
        """delete Player from data base

        Args:
            username (str): username of the player to delete

        Returns:
            bool: True if the Player has been deleted, else False
        """        
        from dao.player_dao import PlayerDao
        return PlayerDao().delete(username)
    
    