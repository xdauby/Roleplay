import unittest
from unittest import TestCase
from business.role.basic_player import BasicPlayer
from business.role.game_master import GameMaster
from dao.game_master_dao import GameMasterDao
from dao.basic_player_dao import BasicPlayerDao
from business.scenario.scenario import Scenario
from business.character.character import Character
from business.user.player import Player
from business.table.table import Table

class TestGameMasterDao(TestCase):
    def test_load_case1(self):
        #case 1 : player has scenario, and he his registered with at some tables
        #GIVEN
        game_master_expected = GameMaster('spiderman')
        
        scenario1 = Scenario(name='The scary movie'
                            , description='Come with us play on a movie'
                            , username='spiderman'
                            , id = 2)
        scenario2 = Scenario(name='Mister robot'
                            , description='Come with us hack computers'
                            , username='spiderman'
                            , id = 3)

        game_master_expected.scenarios.append(scenario1)
        game_master_expected.scenarios.append(scenario2)
        game_master_expected.tables_id.append(2)
        game_master_expected.tables_id.append(22)
        game_master_expected.tables_id.append(41)
        #WHEN
        #spiderman is in the database
        game_master_loaded = GameMasterDao().load('spiderman')
        #THEN
        self.assertEqual(game_master_loaded, game_master_expected)

    def test_load_case2(self):
        #case 1 : player has scenario, and he his not registered with at some tables
        #GIVEN
        game_master_expected = GameMaster('kkj3')
            
        scenario1 = Scenario(name='No imagination'
                                , description='Virtual world using your imagination'
                                , username='kkj3'
                                , id = 5)

        game_master_expected.scenarios.append(scenario1)
        #WHEN
        #kkj3 is in the database
        game_master_loaded = GameMasterDao().load('kkj3')
        #THEN
        self.assertEqual(game_master_loaded, game_master_expected)

    def test_load_case3(self):
    #case 1 : player has no scenario
        game_master_expected = GameMaster('ghostminer')
        #WHEN
        #ghostminer is in the database
        game_master_loaded = GameMasterDao().load('ghostminer')
        #THEN
        self.assertEqual(game_master_loaded, game_master_expected)
    
    def test_add_scenario(self):
        #GIVEN
        # 
        player = Player(firstname='Jean'
                    , lastname='Hill'
                    , username='jacky1'
                    , age=9
                    , game_master=GameMaster(username='jacky1')
                    , basic_player=BasicPlayer(username='jacky1'))
        
        player.save()
        scenario_expected = Scenario(name='test'
                        , description='this is a test'
                        , username='jacky1')            
    
        #WHEN
        added = GameMasterDao().add_scenario(scenario_expected)
        game_master = GameMasterDao().load('jacky1')
        #only one scenario, catch it
        scenario_loaded = game_master.scenarios[0]
        #THEN
        self.assertTrue(added)
        self.assertEqual(scenario_loaded, scenario_expected)

    def test_rm_scenario(self):
        #GIVEN
        player = Player(firstname='Jean'
                    , lastname='Hill'
                    , username='jacky2'
                    , age=9
                    , game_master=GameMaster(username='jacky2')
                    , basic_player=BasicPlayer(username='jacky2'))
        
        player.save()
        
        scenario1 = Scenario(name='test'
                        , description='this is a test'
                        , username='jacky2')            
        
        player.game_master.add_scenario(scenario1)

        game_master_expected = GameMaster(username='jacky2')

        #WHEN
        removed = GameMasterDao().rm_scenario(scenario1.id)
        game_master_loaded = GameMasterDao().load('jacky2')
        #game master must have no scenario because we just deleted it
        
        #THEN
        self.assertTrue(removed)
        self.assertEqual(game_master_loaded, game_master_expected)

        



if __name__ == '__main__':
    unittest.main()