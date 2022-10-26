from business.user.abstract_user import User
from business.user.game_master import GameMaster
from business.user.basic_player import BasicPlayer

class Player(User):
    
    def __init__(self, firstname: str, lastname: str, username: str, age: int, game_master: GameMaster=None, basic_player: BasicPlayer=None, tables = None, halfday = None):
        super().__init__(firstname, lastname, username, age)
        
        self.tables = tables
        self.halfday = halfday
        self.basic_player = basic_player
        self.game_master = game_master

    def load_all_tables(self):
        from dao.table_dao import TableDao
        return TableDao().load_all(show_desactive=False)

    @staticmethod
    def load(username:str):
        from dao.player_dao import PlayerDao
        return PlayerDao().load(username)
        
    def save(self):
        from dao.player_dao import PlayerDao
        return PlayerDao().save(self)

    
