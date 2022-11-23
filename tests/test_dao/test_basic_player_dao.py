import unittest
from unittest import TestCase
from business.role.basic_player import BasicPlayer
from dao.basic_player_dao import BasicPlayerDao
from business.character.character import Character
from business.table.table import Table
from business.user.player import Player
from business.role.game_master import GameMaster


class TestBasicPlayerDao(TestCase):
    def test_load1(self)    :
        #GIVEN
        basic_player_expected = BasicPlayer(username='ghostminer')
        
        character1 = Character(name='miner1', 
                              level=12, race='elf', 
                              equipment='pony', 
                              skill='medicine', 
                              username='ghostminer',
                              id=7)
        
        character2 = Character(name='miner2', 
                              level=13, race='elf', 
                              equipment='pony', 
                              skill='medicine', 
                              username='ghostminer',
                              id=8)
        
        character3 = Character(name='miner3', 
                              level=14, race='elf', 
                              equipment='pony', 
                              skill='medicine', 
                              username='ghostminer',
                              id=9)
                            

    
        basic_player_expected.characters.append(character1)
        basic_player_expected.characters.append(character2)
        basic_player_expected.characters.append(character3)

    
        #WHEN
        #ghostminer is in the database
        basic_player_loaded = BasicPlayerDao().load('ghostminer')
        #THEN
        self.assertEqual(basic_player_loaded, basic_player_expected)

    def test_load2(self)    :
        #GIVEN
        basic_player_expected = BasicPlayer(username='sephix')
        
        character1 = Character(name='battler', 
                              level=17, race='gnome', 
                              equipment='backpack', 
                              skill='nature', 
                              username='sephix',
                              id=2)
        
        basic_player_expected.characters.append(character1)
       
    
        #WHEN
        #sephix is in the database
        basic_player_loaded = BasicPlayerDao().load('sephix')
        #THEN
        
        self.assertEqual(basic_player_loaded, basic_player_expected)

    def test_load3(self)    :
        #GIVEN
        basic_player_expected = BasicPlayer(username='Jo89')
        #WHEN
        #sephix is in the database
        basic_player_loaded = BasicPlayerDao().load('Jo89')
        #THEN 
        self.assertEqual(basic_player_loaded, basic_player_expected)
    
    def test_add_character(self):
        #GIVEN
        player = Player(firstname='Jean'
                    , lastname='Hill'
                    , username='jacky1'
                    , age=9
                    , game_master=GameMaster(username='jacky1')
                    , basic_player=BasicPlayer(username='jacky1'))
        
        player.save()
        character_expected = Character(name='battler', 
                              level=17, race='wizard', 
                              equipment='backpack', 
                              skill='breastplate', 
                              username='jacky1')           
    
        #WHEN
        added = BasicPlayerDao().add_character(character_expected)
        basic_player = BasicPlayerDao().load('jacky1')
        #only one character, let's catch it
        character_loaded = basic_player.characters[0]
        #THEN
        self.assertTrue(added)
        self.assertEqual(character_loaded, character_expected)
        #free db
        Player.delete('jacky1')
    
    def test_rm_character(self):
        #GIVEN
        player = Player(firstname='Jean'
                    , lastname='Hill'
                    , username='jacky2'
                    , age=9
                    , game_master=GameMaster(username='jacky2')
                    , basic_player=BasicPlayer(username='jacky2'))
        
        player.save()
        
        character = Character(name='battler', 
                              level=17, race='wizard', 
                              equipment='backpack', 
                              skill='breastplate', 
                              username='jacky2')                   
        
        player.basic_player.add_character(character)
        basic_player_expected = BasicPlayer(username='jacky2')

        #WHEN
        removed = BasicPlayerDao().rm_character(character.id)
        basic_player_loaded = BasicPlayerDao().load('jacky2')
        #THEN
        self.assertTrue(removed)
        self.assertEqual(basic_player_loaded, basic_player_expected)
        #free db
        Player.delete('jacky2')

if __name__ == '__main__':
    #please, reinitialize the database before the test

    unittest.main()