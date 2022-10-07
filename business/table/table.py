from business.user.abstract_player import Player

class Table:

    def __init__(self, half_day:int, id:int = None) -> None:
        
        self.id = id
        self.half_day = half_day
        self.id_chosen_char = []
        self.game_master = None
        self.basic_player = []

    def add_player(self, player : Player) -> None:
        
        if player.type_player == 'game-master':
            self.game_master = player
            
        if player.type_player == 'basic-player':
            self.basic_player.append(player)

    def rm_player(self, username:str):

        if self.game_master.username == username:
            self.game_master = None
            return

        for i, o in enumerate(self.basic_player):
            if o.username == username:
                del self.basic_player[i]
                break 
        
        
        
