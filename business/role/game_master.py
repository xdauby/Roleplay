from business.scenario.scenario import Scenario

class GameMaster:
    """GameMaster class
        It is the player profile where scenarios are stored.
    """    

    def __init__(self, username:str) -> None:
        """init

        Args:
            username (str): the username player who owns the GameMaster profile
        """        
    
        self.username = username
        self.scenarios = []
    
    def add_scenario(self, scenario: Scenario) -> bool:
        """add a scenario to the GameMaster profile, restricted to 2.

        Args:
            scenario (Scenario): Scenario to add

        Returns:
            bool:  True if the Scenario is added to the profil, else false
        """        
        if len(self.scenarios)<2:
            from dao.game_master_dao import GameMasterDao
            created = GameMasterDao().add_scenario(scenario)
            if created:
                self.scenarios.append(scenario)
                return True
        return False

    def rm_scenario(self, id : int) -> bool:
        """remove scenario from the GameMaster Profile.

        Args:
            id (int): id of the Scenario to remove

        Returns:
            bool: True if the Scenario is removed from the profil, else false
        """        

        for scenario in self.scenarios:
            if scenario.id == id:
                from dao.game_master_dao import GameMasterDao
                if GameMasterDao().rm_scenario(id):
                    self.scenarios.remove(scenario)
                    return True
        return False
    
    def __eq__(self, obj) -> bool:
        if isinstance(obj,GameMaster):
            if self.username == obj.username and self.scenarios == obj.scenarios:
                return True
        return False


    @staticmethod
    def load(username:str):
        """load the GameMaster of player identified by his username.

        Args:
            username (str): username of the player

        Returns:
            GameMaster : return the loaded GameMaster profile
        """        
        from dao.game_master_dao import GameMasterDao
        return GameMasterDao().load(username)
        



