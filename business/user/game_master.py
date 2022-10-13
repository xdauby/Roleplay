from business.user.abstract_player import Player
from business.scenario.scenario import Scenario

class GameMaster(Player):

    def __init__(self, fisrtname:str, lastname:str, username:str, age:int = None) -> None:
        super().__init__(fisrtname, lastname, age, username, 'game-master')
        self.scenarios = []
        self.tables_id = []
        self.tables = []
    
    def add_scenario(self, scenario: Scenario) -> bool:
        
        if len(self.scenarios)<2:
            from dao.scenario_dao import ScenarioDao
            created = ScenarioDao().add(scenario)
            if created:
                self.scenarios.append(scenario)
                return True
        return False

    def rm_scenario(self, id : int) -> bool:

        for i, o in enumerate(self.scenarios):
            if o.id == id:
                from dao.scenario_dao import ScenarioDao
                if ScenarioDao().rm(id):
                    del self.scenarios[i]
                    return True
        return False

    
    @staticmethod
    def load(username:str):
        from dao.game_master_dao import GameMasterDao
        game_master = GameMasterDao().load(username)
        if game_master:
            return game_master
        