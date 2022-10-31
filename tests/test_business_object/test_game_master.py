import unittest
from unittest import TestCase
from business.role.game_master import GameMaster
from business.role.basic_player import BasicPlayer
from business.scenario.scenario import Scenario
from business.table.table import Table
from business.user.player import Player




class TestGameMaster(TestCase):

    #add GameMaster.load(user)

    def test_add_scenario_case1(self):
        #case1 : player have already 2 scenarios
        #GIVEN
        player = Player(firstname='Jean'
                        , lastname='Hill'
                        , username='ninho'
                        , age=9
                        , game_master=GameMaster(username='ninho')
                        , basic_player=BasicPlayer(username='ninho'))
        player.save()
        scenario1 = Scenario(name='test'
                            , description='this is a test'
                            , username='ninho')
        scenario2 = Scenario(name='test2'
                            , description='this is a test'
                            , username='ninho')
        scenario3 = Scenario(name='test3'
                            , description='this is a test'
                            , username='ninho')
        
        player.game_master.add_scenario(scenario1)
        player.game_master.add_scenario(scenario2)


        #WHEN
        added = player.game_master.add_scenario(scenario3)
        #THEN  
        self.assertFalse(added)
    
    def test_add_scenario_case2(self):
        #case1 : player can add the scenario
       #GIVEN
        player = Player(firstname='Jean'
                        , lastname='Hill'
                        , username='ninho2'
                        , age=9
                        , game_master=GameMaster(username='ninho2')
                        , basic_player=BasicPlayer(username='ninho2'))
        player.save()

        scenario1 = Scenario(name='test'
                            , description='this is a test'
                            , username='ninho2')
        scenario2 = Scenario(name='test2'
                            , description='this is a test'
                            , username='ninho2')
        
        player.game_master.add_scenario(scenario1)
        #WHEN
        added = player.game_master.add_scenario(scenario2)
        #THEN  
        self.assertTrue(added)
    
    def test_rm_scenario_case1(self):
        #case1 : wrong id
        #GIVEN
        player = Player(firstname='Jean'
                        , lastname='Hill'
                        , username='ninho3'
                        , age=9
                        , game_master=GameMaster(username='ninho3')
                        , basic_player=BasicPlayer(username='ninho3'))
        player.save()

        scenario1 = Scenario(name='test'
                            , description='this is a test'
                            , username='ninho3')
        
        player.game_master.add_scenario(scenario1)
        id_scenario = -1
        #WHEN
        removed = player.game_master.rm_scenario(id_scenario)
        #THEN  
        self.assertFalse(removed)
    
    def test_rm_scenario_case2(self):
        #case2 : the player can remove his scenario
        #GIVEN
        player = Player(firstname='Jean'
                        , lastname='Hill'
                        , username='ninho4'
                        , age=9
                        , game_master=GameMaster(username='ninho4')
                        , basic_player=BasicPlayer(username='ninho4'))
        player.save()

        scenario1 = Scenario(name='test'
                            , description='this is a test'
                            , username='ninho4')
        
        player.game_master.add_scenario(scenario1)
        id_scenario = scenario1.id
        #WHEN
        removed = player.game_master.rm_scenario(id_scenario)
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
    
    """
    



if __name__ == '__main__':
    #please, reinitialize the database before the test
    unittest.main()
    


