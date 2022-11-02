from business.user.abstract_user import User
from business.role.game_master import GameMaster
from business.role.basic_player import BasicPlayer
from business.notification.notification import Notification

class Player(User):
    
    def __init__(self, firstname: str
                        , lastname: str
                        , username: str
                        , age: int
                        , game_master: GameMaster=None
                        , basic_player: BasicPlayer=None
                        , notification: Notification=None
                        , password:str=''):

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

    def load_player_tables(self) -> None:
        if self.tables:
            from dao.table_dao import TableDao
            return TableDao().load_user_tables(self.tables)

    def load_all_tables(self):
        from dao.table_dao import TableDao
        return TableDao().load_all(show_desactive=False)
        
    def delete_notif(self) -> None:
        from dao.player_dao import PlayerDao
        if PlayerDao().delete_notif(self.username):
            self.notification = None

    def save(self) -> bool: 
        from dao.player_dao import PlayerDao
        return PlayerDao().save(self)

    def __eq__(self, obj):
            if isinstance(obj,Player):
                if self.tables == obj.tables and self.halfday == obj.halfday and self.basic_player == obj.basic_player and self.game_master == obj.game_master and self.firstname == obj.firstname and self.lastname == obj.lastname and self.username == obj.username and self.age == obj.age and self.password == obj.password and self.notification == obj.notification:
                    return True
            return False

    @staticmethod
    def load(username:str):
        from dao.player_dao import PlayerDao
        return PlayerDao().load(username)

    @staticmethod
    def delete(username:str):
        from dao.player_dao import PlayerDao
        return PlayerDao().delete(username)
    
    