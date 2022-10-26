import unittest
from unittest import TestCase
from business.user.basic_player import BasicPlayer
from dao.basic_player_dao import BasicPlayerDao
from business.character.character import Character
from business.table.table import Table

class TestBasicPlayerDao(TestCase):
    def test_add_character_dao(self):
        #GIVEN
        basic_player=BasicPlayer.load('ziak')
        character= Character((name='ziakorak', 
                              level=15, race='bard', 
                              equipment='amulet', 
                              skill='battleaxes', 
                              username='ziak'))
        #WHEN
        added = basic_player_dao.add_character(character)
        #THEN
        self.assertTrue(added)
