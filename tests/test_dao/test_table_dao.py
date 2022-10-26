import unittest
from unittest import TestCase
from business.table.table import Table
from dao.table_dao import TableDao

class TestTableDao(TestCase):

    def test_add_gm_to_table_ok(self):
        # GIVEN
        table_dao = TableDao()
        id_scenario = 3
        id_game = 61
        # WHEN
        add_game_master = table_dao.add_gm_to_table(id_scenario,id_game)
        # THEN
        self.assertEqual(True,add_game_master)

    def test_add_gm_to_table_ko(self):
        # GIVEN
        table_dao = TableDao()
        id_scenario = 3
        id_game = 78
        # WHEN
        add_game_master = table_dao.add_gm_to_table(id_scenario,id_game)
        # THEN
        self.assertFalse(add_game_master)

    def test_add_bp_to_table_ok(self):
        #GIVEN
        table_dao = TableDao()
        id_character = 1
        id_game = 62
        #WHEN
        add_basic_player = table_dao.add_bp_to_table(id_character, id_game)
        #THEN
        self.assertTrue(add_basic_player)

    def test_rm_gm_from_table_ok(self):
         # GIVEN
        table_dao = TableDao()
        id_game = 61
        # WHEN
        rm_game_master = table_dao.rm_gm_from_table(id_game)
        # THEN
        self.assertTrue(rm_game_master)

    def test_rm_bp_from_table_ok(self):
         # GIVEN
        table_dao = TableDao()
        id_character = 1
        id_game = 62
        # WHEN
        rm_basic_player = table_dao.rm_bp_from_table(id_game, id_character)
        # THEN
        self.assertTrue(rm_basic_player)


if __name__ == '__main__':
    unittest.main()