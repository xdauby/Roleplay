from business.user.abstract_player import Player
from business.scenario.scenario import Scenario

class GameMaster(Player):

    def __init__(self, fisrtname:str, lastname:str, username:str, age:int = None) -> None:
        super().__init__(fisrtname, lastname, age, username, 'game-master')
        self.scenarios = []
    
    def add_scenario(self, scenario: Scenario) -> None:
        
        if len(self.scenarios)<2:
            from dao.scenario_dao import ScenarioDao
            created = ScenarioDao().add(scenario)
            if created:
                self.scenarios.append(scenario)
                return True
            else:
                return False

    def rm_scenario(self, name : str) -> None:
        for i, o in enumerate(self.scenarios):
            if o.name == name:
                del self.scenarios[i]
                break

    def load_scen(self) -> None:
        pass

    def load_player_tables(self) -> None:
        pass

    def load_all_tables(self):
        pass
    
    @staticmethod
    def load(username:str):
        from dao.game_master_dao import GameMasterDao
        game_master = GameMasterDao().load(username)
        if game_master:
            return game_master
        