from business.user.game_master import GameMaster
from business.user.basic_player import BasicPlayer

class Table:

    def __init__(self, half_day:int, id:int = None) -> None:
        
        self.id = id
        self.half_day = half_day
        self.id_chosen_char = []
        self.game_master = None
        self.basic_player = []


    def add_gamemaster(self,player: GameMaster, id_scen:int) -> None:
        pass

    def add_basicplayer(self,player: BasicPlayer, id_char:int)-> None:
        pass

    def rm_player(self, username:str) -> None:

        if self.game_master.username == username:
            self.game_master = None
            return

        for i, o in enumerate(self.basic_player):
            if o.username == username:
                del self.basic_player[i]
                break

        #data base actualisation
        
    
    def load_players(self) -> None:
        pass

    def load_char_sce(self) -> None:
        pass
    
    @staticmethod
    def load(table_id : int) -> Table:
        pass



    
    
        
