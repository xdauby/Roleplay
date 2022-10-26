import unittest
from unittest import TestCase
from business.table.table import Table
from business.user.game_master import GameMaster
from business.user.basic_player import BasicPlayer
from business.user.abstract_player import Player

class TestTable(TestCase):

    def test_add_gamemaster_case1(self):
        #case1 : empty table
        #GIVEN
        player = Player.load('batman77')
        id_scenario = 4
        table = Table.load(62)
        #WHEN
        added = table.add_gamemaster(player, id_scenario)
        #THEN  
        self.assertTrue(added)

    def test_add_gamemaster_case2(self):
        #case2 : table has already a gamemaster
        #GIVEN
        game_master = GameMaster.load('batman77')
        id_scenario = 4
        table = Table.load(1)
        #WHEN
        added = table.add_gamemaster(game_master, id_scenario)
        #THEN  
        self.assertFalse(added)

    def test_add_gamemaster_case3(self):
        #case3 : player is registered the same halfday
        #GIVEN
        #spiderman is registered on table 2 (halfday : 1) with a character
        player = Player.load('spiderman')
        id_scenario = 3
        table = Table.load(3)
        #WHEN
        added = table.add_gamemaster(player, id_scenario)
        #THEN  
        self.assertFalse(added)

    def test_add_basic_player_case1(self):
        #case1 : empty table
        #must be false because a player can join a table only if there is a game master
        #GIVEN
        player = Player.load('coximor')
        id_character = 1
        table = Table.load(78)
        #WHEN
        added = table.add_basicplayer(player, id_character)
        #THEN  
        self.assertFalse(added)

    def test_add_basic_player_case2(self):
        #case2 : player registered the same halfday
        #GIVEN
        player = Player.load('sephix')
        id_character = 2
        table = Table.load(2)
        #WHEN
        added = table.add_basicplayer(player, id_character)
        #THEN  
        self.assertFalse(added)

    
    def test_add_basic_player_case3(self):
        #case 3: the number of basic player is 4
        #GIVEN
        player = Player.load('coximor')
        id_character = 1
        table = Table.load(1)
        #WHEN
        added = table.add_basicplayer(player, id_character)
        #THEN  
        self.assertFalse(added)
        pass

    def test_add_basic_player_case4(self):
        #case 4: the player can be added
        #GIVEN
        player = Player.load('coximor')
        id_character = 1
        table = Table.load(2)
        #WHEN
        added = table.add_basicplayer(player, id_character)
        #THEN  
        self.assertTrue(added)

    def test_rm_player_case1(self):
        #case1 : the user is not in the table
        #GIVEN
        table = Table.load(22)
        username = 'coximor'
        #WHEN
        removed = table.rm_player(username)
        #THEN
        self.assertFalse(removed)
    
    def test_rm_player_case2(self):
        #case2 : delete a basic player
        #GIVEN
        table = Table.load(41)
        username = 'coximor'
        #WHEN
        removed = table.rm_player(username)
        #THEN
        self.assertTrue(removed)

    def test_rm_player_case2(self):
        #case3 : delete a game master
        #GIVEN
        table = Table.load(41)
        username = 'spiderman'
        #WHEN
        removed = table.rm_player(username)
        #THEN
        self.assertTrue(removed) 


if __name__ == '__main__':
    #please, reinitialize the database before the test
    unittest.main()



