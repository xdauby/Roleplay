from business.scenario.scenario import Scenario

class GameMaster:

    def __init__(self, firstname:str, lastname:str, username:str, age:int = None) -> None:
        '''initiates a game master
        
        Parameters : 
        firstname : str
        lastname : str
        username : str
        age : int
        '''
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.age = age

        self.scenarios = []
        self.tables_id = []
        self.scenario_table = []
    
    def add_scenario(self, scenario: Scenario) -> bool:
        ''' adds a scenario
        
        Parameters : 
        scenario : Scenario
        
        Returns : bool '''
        if len(self.scenarios)<2:
            from dao.game_master_dao import GameMasterDao
            created = GameMasterDao().add_scenario(scenario)
            if created:
                self.scenarios.append(scenario)
                return True
        return False

    def rm_scenario(self, id : int) -> bool:

        for scenario in self.scenarios:
            if scenario.id == id:
                from dao.game_master_dao import GameMasterDao
                if GameMasterDao().rm_scenario(id):
                    self.scenarios.remove(scenario)
                    return True
        return False

    def load_player_tables(self):
        if self.tables_id:
            from dao.table_dao import TableDao
            return TableDao().load_user_tables(self.tables_id)
    
    
    @staticmethod
    def load(username:str):
        from dao.game_master_dao import GameMasterDao
        return GameMasterDao().load(username)
        