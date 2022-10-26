import unittest
from unittest import TestCase
from business.user.basic_player import BasicPlayer
from dao.basic_player_dao import BasicPlayerDao
from business.character.character import Character
from business.table.table import Table

class TestBasicPlayerDao(TestCase):
    def test_add_character_dao(self)    :
        #GIVEN
        basic_player_1=BasicPlayer.load('ziak')
        character= Character(name='ziakorak', 
                              level=15, race='bard', 
                              equipment='amulet', 
                              skill='battleaxes', 
                              username='ziak')
        
        #WHEN
        basic_player_1.add_character(character)

        basic_player=BasicPlayer.load('ziak')

        basic_player_str=basic_player.__str__()
        basic_player_1_str=basic_player_1.__str__()
        #THEN
        self.assertEqual(basic_player_str,basic_player_1_str)

if __name__ == '__main__':
    unittest.main()