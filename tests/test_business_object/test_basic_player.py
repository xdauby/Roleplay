import unittest
from unittest import TestCase
from business.role.basic_player import BasicPlayer
from business.character.character import Character
from business.table.table import Table
from business.user.player import Player
from business.role.game_master import GameMaster
from business.scenario.scenario import Scenario




class TestBasicPlayer(TestCase):

    def test_add_character_case1(self):
        #case1 : player has already 3 characters
        #GIVEN
        player = Player(firstname='Jean'
                        , lastname='Hill'
                        , username='ninho'
                        , age=9
                        , game_master=GameMaster(username='ninho')
                        , basic_player=BasicPlayer(username='ninho'))
        player.save()
    
        character1 = Character(name='bibi', 
                              level=5, race='bard', 
                              equipment='amulet', 
                              skill='battleaxes', 
                              username='ninho')
        
        character2 = Character(name='bobo', 
                              level=4, race='bard', 
                              equipment='amulet', 
                              skill='battleaxes', 
                              username='ninho')
        
        character3 = Character(name='baba', 
                              level=3, race='bard', 
                              equipment='amulet', 
                              skill='battleaxes', 
                              username='ninho')

        character4 = Character(name='bolobo', 
                              level=8, race='bard', 
                              equipment='amulet', 
                              skill='battleaxes', 
                              username='ninho')

        player.basic_player.add_character(character1)
        player.basic_player.add_character(character2)
        player.basic_player.add_character(character3)
        #WHEN
        added = player.basic_player.add_character(character4)
        #THEN  
        self.assertFalse(added)
        #free db
        Player.delete('ninho')
    
    def test_add_character_case2(self):
        #case2 : player can add the character
        #GIVEN
        player = Player(firstname='Jean'
                        , lastname='Hill'
                        , username='ninho2'
                        , age=9
                        , game_master=GameMaster(username='ninho2')
                        , basic_player=BasicPlayer(username='ninho2'))        
        player.save()
    
        character1 = Character(name='bibi2', 
                              level=5, race='bard', 
                              equipment='amulet', 
                              skill='battleaxes', 
                              username='ninho2')
        
        character2 = Character(name='bobo2', 
                              level=4, race='bard', 
                              equipment='amulet', 
                              skill='battleaxes', 
                              username='ninho2')
        
        character3 = Character(name='baba2', 
                              level=3, race='bard', 
                              equipment='amulet', 
                              skill='battleaxes', 
                              username='ninho2')

        player.basic_player.add_character(character1)
        player.basic_player.add_character(character2)
        #WHEN
        added = player.basic_player.add_character(character3)
        #THEN  
        self.assertTrue(added)
        #free db
        Player.delete('ninho2')

    
    def test_rm_character_case1(self):
        #case1 : wrong id
        #GIVEN

        player = Player(firstname='Jean'
                        , lastname='Hill'
                        , username='ninho3'
                        , age=9
                        , game_master=GameMaster(username='ninho3')
                        , basic_player=BasicPlayer(username='ninho3'))
        player.save()

        character1 = Character(name='bibi3', 
                              level=5, race='bard', 
                              equipment='amulet', 
                              skill='battleaxes', 
                              username='ninho3')
        
        character2 = Character(name='bobo3', 
                              level=4, race='bard', 
                              equipment='amulet', 
                              skill='battleaxes', 
                              username='ninho3')

        player.basic_player.add_character(character1)
        player.basic_player.add_character(character2)

        id_character = -1
        #WHEN
        removed = player.basic_player.rm_character(id_character)
        #THEN  
        self.assertFalse(removed)
        #free db
        Player.delete('ninho3')
    
    def test_rm_character_case2(self):
        #case2 : the player can remove his character
        #GIVEN

        player = Player(firstname='Jean'
                        , lastname='Hill'
                        , username='ninho4'
                        , age=9
                        , game_master=GameMaster(username='ninho4')
                        , basic_player=BasicPlayer(username='ninho4'))        
        player.save()

        character1 = Character(name='bibi4', 
                              level=5, race='bard', 
                              equipment='amulet', 
                              skill='battleaxes', 
                              username='ninho4')
        
        character2 = Character(name='bobo4', 
                              level=4, race='bard', 
                              equipment='amulet', 
                              skill='battleaxes', 
                              username='ninho4')

        player.basic_player.add_character(character1)
        player.basic_player.add_character(character2)

        id_character = character2.id
        #WHEN
        removed = player.basic_player.rm_character(id_character)
        #THEN  
        self.assertTrue(removed)
        #free db
        Player.delete('ninho4')

    def test_rm_character_case3(self):
        #case3 : the player can remove his character, and leave the tables where he is registered with
        #method relative to Table are verified (test in TestTable)
        #GIVEN
        table1 = Table.load(8)

        player1 = Player(firstname='Jean'
                        , lastname='Hill'
                        , username='jacky5'
                        , age=9
                        , game_master=GameMaster(username='jacky5')
                        , basic_player=BasicPlayer(username='jacky5'))

        player2 = Player(firstname='Jean'
                        , lastname='Hill'
                        , username='jacky6'
                        , age=9
                        , game_master=GameMaster(username='jacky6')
                        , basic_player=BasicPlayer(username='jacky6'))

        
        player1.save()
        player2.save()

        scenario1p1 = Scenario(name='test'
                            , description='this is a test'
                            , username='jacky5')
    
        character1p2 = Character(name='huross', 
                              level=5, race='bard', 
                              equipment='amulet', 
                              skill='battleaxes', 
                              username='jacky6')

        player1.game_master.add_scenario(scenario1p1)
        player2.basic_player.add_character(character1p2)
        
        table1.add_gamemaster(player1, scenario1p1.id)
        table1.add_basicplayer(player2, character1p2.id)
        
        expected_table = Table(half_day=1, active=True, id =8)
        expected_table.players.append(player1)
        expected_table.scenario = scenario1p1
        #WHEN
        removed = player2.basic_player.rm_character(character1p2.id)
        #load the table back to test
        table1_loaded = Table.load(8)
        #THEN  
        self.assertTrue(removed)
        self.assertEqual(table1_loaded, expected_table)
        #free db
        Player.delete('jacky6')
        Player.delete('jacky5')

    



if __name__ == '__main__':
    #please, reinitialize the database before the test

    unittest.main()

    
