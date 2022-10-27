from business.user.abstract_user import User
from business.user.game_master import GameMaster
from business.user.basic_player import BasicPlayer
from business.user.abstract_player import Player
from business.table.table import Table

class Organiser(User):
    
    def __init__(self, fisrtname: str, lastname: str, username:str, age:int, id : int = None) -> None:
        super().__init__(fisrtname, lastname, username, age)
        self.id = id

    def load_all_tables(self):
        from dao.table_dao import TableDao
        return TableDao().load_all(show_desactive=True)
        


    def ban(self, username:str):

        player = Player.load(username)
        if player:
            gm = player.game_master.load(username)
            bp = player.basic_player.load(username)
            
            if gm.scenarios:
                for scenerio in gm.scenarios:
                    gm.rm_scenario(scenerio.id)

            if bp.characters:
                for character in bp.characters:
                    bp.rm_character(character.id)
            return True
        return False

    @staticmethod
    def load(username:str):
        from dao.organiser_dao import OrganiserDao
        organiser = OrganiserDao().load(username)
        return organiser
