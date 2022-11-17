import unittest
from unittest import TestCase
from business.table.table import Table
from business.character.character import Character
from business.scenario.scenario import Scenario
from business.role.game_master import GameMaster
from business.role.basic_player import BasicPlayer
from business.user.player import Player
from dao.table_dao import TableDao

class TestTableDao(TestCase):



    def test_load(self):
        #GIVEN
        p1 = Player(firstname='Tim'
                    , lastname='Mossuz'
                    , username='spiderman'
                    , age=19
                    , password='5cc55633769b725e714f9cdfc6c611e11e95bcb0f4f642ac922a373f0c91d055')

        game_master_p1 = GameMaster(username='spiderman')
        basic_player_p1 = BasicPlayer(username='spiderman')
        
        scen1p1 = Scenario(name='The scary movie'
                            , description='Come with us play on a movie'
                            , id=2 
                            , username='spiderman')

        scen2p1 = Scenario(name='Mister robot'
                            , description='Come with us hack computers'
                            , id=3 
                            , username='spiderman')

        game_master_p1.scenarios.append(scen1p1)
        game_master_p1.scenarios.append(scen2p1)

        char1p1 = Character(name='spider'
                            , level=10
                            , race='rogue'
                            , equipment='pony'
                            , skill='longswords'
                            , id=6
                            , username='spiderman')

        basic_player_p1.characters.append(char1p1)

        p1.game_master = game_master_p1
        p1.basic_player = basic_player_p1
        p1.tables = [41,2,22]
        p1.halfday = [3,1,2]


        p2 = Player(firstname='Jean'
                    , lastname='Valjean'
                    , username='kkj3'
                    , age=19
                    , password='5cc55633769b725e714f9cdfc6c611e11e95bcb0f4f642ac922a373f0c91d055')


        game_master_p2 = GameMaster(username='kkj3')
        basic_player_p2 = BasicPlayer(username='kkj3')
        
        scen1p2 = Scenario(name='No imagination'
                            , description='Virtual world using your imagination'
                            , id=5 
                            , username='kkj3')
        
        game_master_p2.scenarios.append(scen1p2)

        char1p2 = Character(name='cafe'
                            , level=3
                            , race='rogue'
                            , equipment='pony'
                            , skill='longswords'
                            , id=4
                            , username='kkj3')

        char2p2 = Character(name='rocketluri'
                            , level=5
                            , race='rogue'
                            , equipment='pony'
                            , skill='longswords'
                            , id=5
                            , username='kkj3')

        basic_player_p2.characters.append(char1p2)
        basic_player_p2.characters.append(char2p2)

        p2.basic_player = basic_player_p2
        p2.game_master = game_master_p2
        p2.tables = [42, 2]
        p2.halfday = [3, 1]
    
        expected_table = Table(half_day=1, active=True, id=2)
        expected_table.scenario = scen1p1
        expected_table.characters.append(char1p2)
        expected_table.players.append(p1)
        expected_table.players.append(p2)
        
        #WHEN
        loaded_table = TableDao().load(2)
        #THEN
        self.assertEqual(loaded_table, expected_table)  


    def test_add_gm_to_table_ok(self):
        # GIVEN

        p1 = Player(firstname='Tim'
                    , lastname='Mossuz'
                    , username='jack1'
                    , age=19
                    , password='5cc55633769b725e714f9cdfc6c611e11e95bcb0f4f642ac922a373f0c91d055')
        p1.save()

        game_master_p1 = GameMaster(username='jack1')
        basic_player_p1 = BasicPlayer(username='jack1')
        
        scen1p1 = Scenario(name='The scary movie'
                            , description='Come with us play on a movie'
                            , username='jack1')

        game_master_p1.add_scenario(scen1p1)

        p1.game_master = game_master_p1
        p1.basic_player = basic_player_p1
        p1.tables = [28]
        p1.halfday = [2]

        id_scenario = scen1p1.id
        id_game = 28

        expected_table = Table(half_day=2
                                , active=True
                                , id=28)
        
        expected_table.scenario = scen1p1
        expected_table.players.append(p1)
    
        # WHEN
        add_game_master = TableDao().add_gm_to_table(id_scenario,id_game)
        loaded_table_after_added_gm = TableDao().load(id_game)

        # THEN
        self.assertEqual(True,add_game_master)
        self.assertEqual(loaded_table_after_added_gm,expected_table)
        #clean db
        Player.delete('jack1')

    def test_add_bp_to_table_ok(self):
        #GIVEN
        p1 = Player(firstname='Tim'
                    , lastname='Mossuz'
                    , username='jack2'
                    , age=19
                    , password='5cc55633769b725e714f9cdfc6c611e11e95bcb0f4f642ac922a373f0c91d055')
        p1.save()

        game_master_p1 = GameMaster(username='jack2')
        basic_player_p1 = BasicPlayer(username='jack2')
        
        scen1p1 = Scenario(name='The scary movie'
                            , description='Come with us play on a movie'
                            , username='jack2')

        game_master_p1.add_scenario(scen1p1)

        p1.game_master = game_master_p1
        p1.basic_player = basic_player_p1
        p1.tables = [27]
        p1.halfday = [2]

        p2 = Player(firstname='Jean'
                    , lastname='Valjean'
                    , username='jack3'
                    , age=19
                    , password='5cc55633769b725e714f9cdfc6c611e11e95bcb0f4f642ac922a373f0c91d055')
        p2.save()

        game_master_p2 = GameMaster(username='jack3')
        basic_player_p2 = BasicPlayer(username='jack3')
        
        char1p2 = Character(name='cafej2'
                            , level=3
                            , race='rogue'
                            , equipment='pony'
                            , skill='longswords'
                            , id=4
                            , username='jack3')


        basic_player_p2.add_character(char1p2)

        p2.basic_player = basic_player_p2
        p2.game_master = game_master_p2
        p2.tables = [27]
        p2.halfday = [2]

        id_char = char1p2.id
        id_scenario = scen1p1.id
        id_game = 27

        expected_table = Table(half_day=2
                                , active=True
                                , id=27)
        
        expected_table.scenario = scen1p1
        expected_table.characters.append(char1p2)
        expected_table.players.append(p1)
        expected_table.players.append(p2)

        #update the table in db
        TableDao().add_gm_to_table(id_scenario,id_game)

        # WHEN
        add_basic_player = TableDao().add_bp_to_table(id_char,id_game)
        loaded_table_after_added_bp = TableDao().load(id_game)
        #THEN
        self.assertEqual(True,add_basic_player)
        self.assertEqual(loaded_table_after_added_bp.players,expected_table.players)
        #clean db
        Player.delete('jack2')
        Player.delete('jack3')

    def test_rm_bp_from_table_ok(self):
         #GIVEN
        p1 = Player(firstname='Tim'
                    , lastname='Mossuz'
                    , username='jack2'
                    , age=19
                    , password='5cc55633769b725e714f9cdfc6c611e11e95bcb0f4f642ac922a373f0c91d055')
        p1.save()

        game_master_p1 = GameMaster(username='jack2')
        basic_player_p1 = BasicPlayer(username='jack2')
        
        scen1p1 = Scenario(name='The scary movie'
                            , description='Come with us play on a movie'
                            , username='jack2')

        game_master_p1.add_scenario(scen1p1)

        p1.game_master = game_master_p1
        p1.basic_player = basic_player_p1
        p1.tables = [27]
        p1.halfday = [2]

        p2 = Player(firstname='Jean'
                    , lastname='Valjean'
                    , username='jack3'
                    , age=19
                    , password='5cc55633769b725e714f9cdfc6c611e11e95bcb0f4f642ac922a373f0c91d055')
        p2.save()

        game_master_p2 = GameMaster(username='jack3')
        basic_player_p2 = BasicPlayer(username='jack3')
        
        char1p2 = Character(name='cafej2'
                            , level=3
                            , race='rogue'
                            , equipment='pony'
                            , skill='longswords'
                            , id=4
                            , username='jack3')


        basic_player_p2.add_character(char1p2)

        p2.basic_player = basic_player_p2
        p2.game_master = game_master_p2
        p2.tables = [27]
        p2.halfday = [2]

        id_char = char1p2.id
        id_scenario = scen1p1.id
        id_game = 27

        expected_table = Table(half_day=2
                                , active=True
                                , id=27)
        
        expected_table.scenario = scen1p1
        expected_table.players.append(p1)

        #update the table in db
        TableDao().add_gm_to_table(id_scenario,id_game)
        TableDao().add_bp_to_table(id_char,id_game)
        # WHEN
        rm_bp = TableDao().rm_bp_from_table(id_game, id_char)
        loaded_table_after_rm_bp = TableDao().load(id_game)
        #THEN
        self.assertEqual(True,rm_bp)
        self.assertEqual(loaded_table_after_rm_bp,expected_table)

        #clean db
        Player.delete('jack2')
        Player.delete('jack3')

    def test_rm_gm_from_table_ok(self):
        #GIVEN
        p1 = Player(firstname='Tim'
                    , lastname='Mossuz'
                    , username='jack2'
                    , age=19
                    , password='5cc55633769b725e714f9cdfc6c611e11e95bcb0f4f642ac922a373f0c91d055')
        p1.save()

        game_master_p1 = GameMaster(username='jack2')
        basic_player_p1 = BasicPlayer(username='jack2')
        
        scen1p1 = Scenario(name='The scary movie'
                            , description='Come with us play on a movie'
                            , username='jack2')

        game_master_p1.add_scenario(scen1p1)

        p1.game_master = game_master_p1
        p1.basic_player = basic_player_p1
        p1.tables = [27]
        p1.halfday = [2]

        id_scenario = scen1p1.id
        id_game = 27

        expected_table = Table(half_day=2
                                , active=True
                                , id=27)
        
        #update the table in db
        TableDao().add_gm_to_table(id_scenario,id_game)
        # WHEN
        rm_gm = TableDao().rm_gm_from_table(id_game)
        loaded_table_after_rm_gm = TableDao().load(id_game)
        #THEN
        self.assertEqual(True,rm_gm)
        self.assertEqual(loaded_table_after_rm_gm,expected_table)

        #clean db
        Player.delete('jack2')


    def test_active_table(self):

        #GIVEN
        expected_table = Table(half_day=2, active=True, id=31)

        #WHEN
        #table 31 is desactivated in db
        actived = TableDao().active_table(31)
        loaded_table_after_activate_it = TableDao().load(31)
        #THEN
        self.assertEqual(True,actived)
        self.assertEqual(loaded_table_after_activate_it,expected_table)

        #desactivate it back
        TableDao().desactive_table(31)

    def test_desactive_table(self):

        #GIVEN
        expected_table = Table(half_day=2, active=False, id=30)

        #WHEN
        #table 30 is activated in db
        desactived = TableDao().desactive_table(30)
        loaded_table_after_desactivate_it = TableDao().load(30)
        #THEN
        self.assertEqual(True,desactived)
        self.assertEqual(loaded_table_after_desactivate_it,expected_table)

        #activate it back
        TableDao().active_table(30)

if __name__ == '__main__':
    #please, reinitialize the database before the test
    unittest.main()
      