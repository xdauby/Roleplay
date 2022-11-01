import unittest
from unittest import TestCase
from business.role.basic_player import BasicPlayer
from business.role.game_master import GameMaster
from business.scenario.scenario import Scenario
from business.character.character import Character
from business.user.player import Player
from business.table.table import Table
from dao.player_dao import PlayerDao
from business.notification.notification import Notification

class TestPlayerDao(TestCase):
    def test_load_case1(self):
        #case 1 : player has scenario(s), character(s) and tables
        #GIVEN
        game_master = GameMaster('spiderman')
        basic_player = BasicPlayer('spiderman')

        scenario1 = Scenario(name='The scary movie'
                            , description='Come with us play on a movie'
                            , username='spiderman'
                            , id = 2)
        scenario2 = Scenario(name='Mister robot'
                            , description='Come with us hack computers'
                            , username='spiderman'
                            , id = 3)

        character1 = Character(name='spider', 
                              level=10, race='rogue', 
                              equipment='pony', 
                              skill='longswords', 
                              username='spiderman',
                              id=6)
                
        game_master.scenarios.append(scenario1)
        game_master.scenarios.append(scenario2)
        game_master.tables_id.append(2)
        game_master.tables_id.append(22)
        game_master.tables_id.append(41)
        basic_player.characters.append(character1)

        player_expected = Player(firstname='Tim'
                                , lastname='Mossuz'
                                , username='spiderman'
                                , age=19
                                , game_master=game_master
                                , basic_player=basic_player
                                , password ='5cc55633769b725e714f9cdfc6c611e11e95bcb0f4f642ac922a373f0c91d055')

        player_expected.tables.append(2)
        player_expected.tables.append(22)
        player_expected.tables.append(41)
        player_expected.halfday.append(3)
        player_expected.halfday.append(1)
        player_expected.halfday.append(2)
        


        #WHEN
        #spiderman is in the database
        player_loaded = PlayerDao().load('spiderman')
        #THEN
        self.assertEqual(player_loaded, player_expected)

    def test_load_case2(self):
        #case 2 : player has characters and tables
        #GIVEN
        basic_player = BasicPlayer(username='ghostminer')
        game_master = GameMaster('ghostminer')

        character1 = Character(name='miner1', 
                              level=12, race='rogue', 
                              equipment='pony', 
                              skill='longswords', 
                              username='ghostminer',
                              id=7)
        
        character2 = Character(name='miner2', 
                              level=13, race='rogue', 
                              equipment='pony', 
                              skill='longswords', 
                              username='ghostminer',
                              id=8)
        
        character3 = Character(name='miner3', 
                              level=14, race='rogue', 
                              equipment='pony', 
                              skill='longswords', 
                              username='ghostminer',
                              id=9)

        basic_player.characters.append(character1)
        basic_player.characters.append(character2)
        basic_player.characters.append(character3)
        basic_player.tables_id.append(1)
        basic_player.tables_id.append(41)

        player_expected = Player(firstname='amine'
                                , lastname='ru'
                                , username='ghostminer'
                                , age=19
                                , game_master=game_master
                                , basic_player=basic_player
                                , password ='5cc55633769b725e714f9cdfc6c611e11e95bcb0f4f642ac922a373f0c91d055' )

        player_expected.halfday.append(3)
        player_expected.halfday.append(1)
        player_expected.tables.append(1)
        player_expected.tables.append(41)
        #WHEN
        #ghostminer is in the database
        player_loaded = PlayerDao().load('ghostminer')
        #THEN
        self.assertEqual(player_loaded, player_expected)

    def test_load_case3(self):
        #case 3 : player has scenarios and tables
        #GIVEN

        game_master = GameMaster(username='Jo89')
        basic_player = BasicPlayer(username='Jo89')

        scenario1 = Scenario(name='A bad trip'
                                , description='Come get ayahuasca'
                                , username='Jo89'
                                , id = 6)

        game_master.scenarios.append(scenario1)
        game_master.tables_id.append(42)
    
        player_expected = Player(firstname='Antoine'
                                , lastname='De Paepe'
                                , username='Jo89'
                                , age=19
                                , game_master=game_master
                                , basic_player=basic_player
                                , password ='5cc55633769b725e714f9cdfc6c611e11e95bcb0f4f642ac922a373f0c91d055' )
        
        player_expected.halfday.append(3)
        player_expected.tables.append(42)
        #WHEN
        #Jo89 is in the database
        player_loaded = PlayerDao().load('Jo89')
        #THEN
        self.assertEqual(player_loaded, player_expected)

    def test_load_case4(self):
        #case 4 : player has no scenario and no character
        #GIVEN
        game_master = GameMaster(username='ziakbis')
        basic_player = BasicPlayer(username='ziakbis')
        
        player_expected = Player(firstname='George'
                                , lastname='Grand'
                                , username='ziakbis'
                                , age=19
                                , game_master=game_master
                                , basic_player=basic_player
                                , password ='5cc55633769b725e714f9cdfc6c611e11e95bcb0f4f642ac922a373f0c91d055' )
    
        #WHEN
        #Jo89 is in the database
        player_loaded = PlayerDao().load('ziakbis')
        #THEN
        self.assertEqual(player_loaded, player_expected)

    def test_player_halfday_case1(self):
        #case 1 : player has halfday
        #GIVEN
        expected_halfday = [3]
        #WHEN
        #Jo89 is in the database
        halfday_loaded = PlayerDao().player_halfday('Jo89')
        #THEN
        self.assertEqual(halfday_loaded, expected_halfday)

    def test_player_halfday_case2(self):
        #case 1 : player has no halfday
        #GIVEN
        expected_halfday = []
        #WHEN
        #ziakbis is in the database
        halfday_loaded = PlayerDao().player_halfday('ziakbis')
        #THEN
        self.assertEqual(halfday_loaded, expected_halfday)

    def test_save(self):
        #GIVEN
        game_master = GameMaster('lolit')
        basic_player = BasicPlayer('lolit')
        player = Player(firstname='jean'
                                , lastname='jacques'
                                , username='lolit'
                                , age=19
                                , game_master=game_master
                                , basic_player=basic_player
                                , password ='5cc55633769b725e714f9cdfc6c611e11e95bcb0f4f642ac922a373f0c91d055' )
        
        #WHEN
        created = player.save()
        player_loaded = PlayerDao().load('lolit')
        #THEN
        self.assertEqual(player_loaded, player)

    def test_load_notif(self):
        #GIVEN
        notif = Notification(notification= 'You have been moved, check your tables !'
                            , username= 'coximor'
                            , id = 1) 
        #WHEN
        notif_loaded = PlayerDao().load_notif('coximor')
        #THEN
        self.assertEqual(notif_loaded, notif)





if __name__ == '__main__':
    unittest.main()