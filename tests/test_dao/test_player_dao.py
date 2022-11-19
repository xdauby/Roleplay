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
from dao.organiser_dao import OrganiserDao

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
                              level=10, race='elf', 
                              equipment='pony', 
                              skill='medicine', 
                              username='spiderman',
                              id=6)
                
        game_master.scenarios.append(scenario1)
        game_master.scenarios.append(scenario2)
        basic_player.characters.append(character1)

        player_expected = Player(firstname='Tim'
                                , lastname='Mossuz'
                                , username='spiderman'
                                , age=19
                                , game_master=game_master
                                , basic_player=basic_player
                                , password ='5cc55633769b725e714f9cdfc6c611e11e95bcb0f4f642ac922a373f0c91d055')
        
        player_expected.tables.append(41)
        player_expected.tables.append(2)
        player_expected.tables.append(22)
        
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

        basic_player.characters.append(character1)
        basic_player.characters.append(character2)
        basic_player.characters.append(character3)

        player_expected = Player(firstname='amine'
                                , lastname='ru'
                                , username='ghostminer'
                                , age=19
                                , game_master=game_master
                                , basic_player=basic_player
                                , password ='5cc55633769b725e714f9cdfc6c611e11e95bcb0f4f642ac922a373f0c91d055' )

        player_expected.halfday.append(3)
        player_expected.halfday.append(1)
        player_expected.tables.append(41)
        player_expected.tables.append(1)
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

    def test_player_halfday_and_tables_id_case1(self):
        #case 1 : player has halfday and tables
        #GIVEN
        expected_halfday = [3]
        expected_tables = [42]
        expected_halfday_tables = {'halfday' : expected_halfday, 'tables_id': expected_tables}
        #WHEN
        #Jo89 is in the database
        halfday_loaded = PlayerDao().player_halfday_and_tables_id('Jo89')
        #THEN
        self.assertEqual(halfday_loaded, expected_halfday_tables)

    def test_player_halfday_and_tables_id_case2(self):
        #case 1 : player has no halfday and tables
        #GIVEN
        expected_halfday_tables = {'halfday' : [], 'tables_id': []}
        #WHEN
        #ziakbis is in the database
        halfday_loaded = PlayerDao().player_halfday_and_tables_id('ziakbis')
        #THEN
        self.assertEqual(halfday_loaded, expected_halfday_tables)

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
        #free db
        Player.delete('lolit')

    def test_load_notif(self):
        #GIVEN
        notif = Notification(notification= 'You have been moved, check your tables !'
                            , username= 'coximor'
                            , id = 1) 
        #WHEN
        notif_loaded = PlayerDao().load_notif('coximor')
        #THEN
        self.assertEqual(notif_loaded, notif)

    def test_delete_notif(self):
        #GIVEN
        game_master = GameMaster(username='zrk')
        basic_player = BasicPlayer(username='zrk')
        
        notif = Notification(notification= 'You have been moved, check your tables !'
                            , username= 'zrk')

        expected_player = Player(firstname='George'
                                , lastname='Grand'
                                , username='zrk'
                                , age=19
                                , game_master=game_master
                                , basic_player=basic_player
                                , password ='5cc55633769b725e714f9cdfc6c611e11e95bcb0f4f642ac922a373f0c91d055')

        expected_player.save()
        
        OrganiserDao().save_notif(notif)
        #at this step, the notif is in the db

        #WHEN
        deleted = PlayerDao().delete_notif('zrk')
        player_loaded = Player.load('zrk')
        #THEN
        self.assertTrue(deleted)
        self.assertEqual(expected_player, player_loaded)
        #free db
        Player.delete('zrk')

    def test_delete(self):
        #GIVEN
        table1 = Table.load(8)
        table2 = Table.load(25)

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
        
        player3 = Player(firstname='Jean'
                        , lastname='Hill'
                        , username='jacky7'
                        , age=9
                        , game_master=GameMaster(username='jacky7')
                        , basic_player=BasicPlayer(username='jacky7'))
        
        player1.save()
        player2.save()
        player3.save()     

        scenario1p1 = Scenario(name='test'
                            , description='this is a test'
                            , username='jacky5')

        scenario1p2 = Scenario(name='test2'
                            , description='this is a test'
                            , username='jacky6')

        scenario1p3 = Scenario(name='test2'
                            , description='this is a test'
                            , username='jacky7')

        character1p2 = Character(name='huross', 
                              level=5, race='bard', 
                              equipment='amulet', 
                              skill='battleaxes', 
                              username='jacky6')

        character1p3 = Character(name='hugobosss', 
                              level=5, race='bard', 
                              equipment='amulet', 
                              skill='battleaxes', 
                              username='jacky7')
        
        player1.game_master.add_scenario(scenario1p1)    

        player2.game_master.add_scenario(scenario1p2)
        player2.basic_player.add_character(character1p2)

        player3.game_master.add_scenario(scenario1p3)
        player3.basic_player.add_character(character1p3)

        table1.add_gamemaster(player2, scenario1p2.id)
        table1.add_basicplayer(player3, character1p3.id)

        table2.add_gamemaster(player1, scenario1p1.id)
        table2.add_basicplayer(player2, character1p2.id)

        #expected tables after deleted player2


        #table id 8 must be empyt
        table1_expected = Table(half_day=1, active=True, id=8)

        #table id 25 only have game master player 1 
        table2_expected = Table(half_day=2, active=True, id=25)
        table2_expected.players.append(player1)
        table2_expected.scenario = scenario1p1

    
        #WHEN
        deleted = player1.delete('jacky6')

        table1_loaded = Table.load(8)
        table2_loaded = Table.load(25)
        #THEN
        self.assertTrue(deleted)
        self.assertEqual(table1_expected, table1_loaded)
        self.assertEqual(table2_expected, table2_loaded)
        #free db
        Player.delete('jacky5')
        Player.delete('jacky6')
        Player.delete('jacky7')



if __name__ == '__main__':
    #please, reinitialize the database before the test
    unittest.main()