from business.user.game_master import GameMaster
from business.user.basic_player import BasicPlayer

class Table:

    def __init__(self, half_day:int, id:int = None) -> None:
        
        self.id = id
        self.half_day = half_day
        self.game_master = None
        self.basic_player = []

    def add_gamemaster(self, player: GameMaster, id_scen:int) -> None:

        if self.game_master:
            self.game_master = player

    def add_basicplayer(self,player: BasicPlayer, id_char:int)-> None:
        
        if len(self.basic_player) < 4:
            self.basic_player.append(player)
        

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

    def load_char_scen(self) -> None:
        pass
    
    @staticmethod
    def load(table_id : int):
        pass

    def __str__(self) -> str:

        player_str = ''

        for player in self.basic_player:
            player_str += f'{player.username} with Character {player.characters[0].name} \n'

        view = f'Table id : {self.id} \n Game Master : {self.game_master.username} with Scenario {self.game_master.scenarios[0].name}\n' + player_str
        return view

    
    
        
