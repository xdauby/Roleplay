import unittest
from unittest import TestCase
from business.user.game_master import GameMaster
from business.scenario.scenario import Scenario
from business.table.table import Table




class TestGameMaster(TestCase):

    #add GameMaster.load(user)

    def test_add_scenario_case1(self):
        #case1 : player have already 2 scenarios
        #GIVEN
        game_master = GameMaster.load('spiderman')
        scenario = Scenario('test', 'this is a test',username='spiderman')
        #WHEN
        added = game_master.add_scenario(scenario)
        #THEN  
        self.assertFalse(added)
    
    def test_add_scenario_case2(self):
        #case1 : player can add the scenario
        #GIVEN
        game_master = GameMaster.load('ghostminer')
        scenario = Scenario('test', 'this is a test',username='ghostminer')
        #WHEN
        added = game_master.add_scenario(scenario)
        #THEN  
        self.assertTrue(added)
    
    def test_rm_scenario_case1(self):
        #case1 : wrong id
        #GIVEN
        game_master = GameMaster.load('sephix')
        id_scenario = -1
        #WHEN
        removed = game_master.rm_scenario(id_scenario)
        #THEN  
        self.assertFalse(removed)
    
    def test_rm_scenario_case2(self):
        #case2 : the player can remove his scenario
        #GIVEN
        game_master = GameMaster.load('ghostminer')
        #ghostminer has 0 scenario, so we catch the id in that way
        id_scenario = game_master.scenarios[0].id
        #WHEN
        removed = game_master.rm_scenario(id_scenario)
        #THEN  
        self.assertTrue(removed)
    """
    def test_rm_scenario_case3(self):
        #case3 : the player can remove his scenario, and leave the tables where he is registered with
        #method relative to Table are verified (test in TestTable)
        #GIVEN
        #Artificially add a scenario and connect him to a table
        game_master = GameMaster.load('ghostminer')
        scenario = Scenario('test', 'this is a test',username='ghostminer')
        game_master.add_scenario(scenario)
        id_scenario = scenario.id
        #add the game master with the scenario
        table = Table.load(23)
        table.add_gamemaster(game_master, id_scenario)
        
        #WHEN
        removed = game_master.rm_scenario(id_scenario)
        #load the table back to test
        table = Table.load(23)
        table_str = table.__str__()

        #THEN  
        self.assertTrue(removed)
        self.assertEqual(table_str, 'Table id : 23, half day : 2, acivate : True, table empty.')
    
    def test_load_player_tables(self):
        #GIVEN
        game_master = GameMaster.load('Jo89')
        #WHEN
        tables = game_master.load_player_tables()
        #Jo89 has only one table as game master
        table_str = tables[0].__str__()

        #THEN  
        self.assertEqual(table_str, '\nTable id : 42, half day : 3, acivate : True \n' \
                                    ' Game Master : Jo89 with Scenario A bad trip\n'\
                                    'kkj3 with Character cafe \n')
    """
    



if __name__ == '__main__':
    #please, reinitialize the database before the test
    unittest.TestLoader.sortTestMethodsUsing = None
    unittest.main()
    


