import unittest
from unittest import TestCase
from business.user.basic_player import BasicPlayer
from business.character.character import Character
from business.table.table import Table
from business.user.abstract_player import Player
from business.user.game_master import GameMaster




class TestBasicPlayer(TestCase):

    #add BasicPlayer.load(user) test

    def test_add_character_case1(self):
        #case1 : player has already 3 characters
        #GIVEN
        player = Player(firstname='Jean', lastname='Hill', username='ninho', age=9)
        player.save()
        player.game_master = GameMaster(firstname='Jean', lastname='Hill', username='ninho')
        player.basic_player = BasicPlayer(firstname='Jean', lastname='Hill', username='ninho')

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
    
    def test_add_character_case2(self):
        #case2 : player can add the character
        #GIVEN
        player = Player(firstname='Jean', lastname='Hill', username='ninho', age=9)
        player.save()
        player.game_master = GameMaster(firstname='Jean', lastname='Hill', username='ninho')
        player.basic_player = BasicPlayer(firstname='Jean', lastname='Hill', username='ninho')

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

        player.basic_player.add_character(character1)
        player.basic_player.add_character(character2)
        #WHEN
        added = player.basic_player.add_character(character3)
        #THEN  
        self.assertTrue(added)
    
    def test_rm_character_case1(self):
        #case1 : wrong id
        #GIVEN
        basic_player = BasicPlayer.load('ghostminer')
        id_character = -1
        #WHEN
        removed = basic_player.rm_character(id_character)
        #THEN  
        self.assertFalse(removed)
    
    def test_rm_character_case2(self):
        #case2 : the player can remove his character
        #GIVEN
        basic_player = BasicPlayer.load('Jo89')
        #Jo89 has only one basic player, the one created before 
        id_character = basic_player.characters[0].id
        #WHEN
        removed = basic_player.rm_character(id_character)
        #THEN  
        self.assertTrue(removed)

    def test_rm_character_case3(self):
        #case3 : the player can remove his character, and leave the tables where he is registered with
        #method relative to Table are verified (test in TestTable)
        #GIVEN
        #Artificially add a character and connect him to a table
        player = Player.load('Jo89')
        basic_player = player.basic_player
        character = Character(name='bibi', 
                              level=5, race='bard', 
                              equipment='amulet', 
                              skill='battleaxes', 
                              username='Jo89')
        basic_player.add_character(character)
        id_character = character.id
        #add the basic player with the character
        table = Table.load(22)
        table.add_basicplayer(player, id_character)
        
        #WHEN
        removed = basic_player.rm_character(id_character)
        #load the table back to test
        table = Table.load(22)
        table_str = table.__str__()
        #THEN  
        self.assertTrue(removed)
        self.assertEqual(table_str, '\nTable id : 22, half day : 2, acivate : True \n' \
                                    ' Game Master : spiderman with Scenario The scary movie\n'\
                                    'paya6 with Character pinguin \n')


    



if __name__ == '__main__':
    #please, reinitialize the database before the test
    #unittest.TestLoader.sortTestMethodsUsing = None
    #unittest.main()
    TestBasicPlayer().test_add_character_case1()
    
