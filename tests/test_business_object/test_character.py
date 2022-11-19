from business.character.character import Character
import unittest
from unittest import TestCase




class TestBasicPlayer(TestCase):

    def test_check_race1(self):
        #GIVEN
        character = Character(name='huross', 
                              level=5, race='elf', 
                              equipment='amulet', 
                              skill='arcana', 
                              username='jacky6')
        #WHEN
        check = character.check_race()
        #THEN
        self.assertTrue(check)

    def test_check_race2(self):
        #GIVEN
        character = Character(name='huross', 
                              level=5, race='this race doesn\'t exist', 
                              equipment='amulet', 
                              skill='arcana', 
                              username='jacky6')
        #WHEN
        check = character.check_race()
        #THEN
        self.assertFalse(check)
    def test_check_equipment1(self):
        #GIVEN
        character = Character(name='huross', 
                              level=5, race='elf', 
                              equipment='amulet', 
                              skill='arcana', 
                              username='jacky6')
        #WHEN
        check = character.check_equipment()
        #THEN
        self.assertTrue(check)
    def test_check_equipment2(self):
        #GIVEN
        character = Character(name='huross', 
                              level=5, race='elf', 
                              equipment='this equipment doesn\'t exist', 
                              skill='arcana', 
                              username='jacky6')
        #WHEN
        check = character.check_equipment()
        #THEN
        self.assertFalse(check)
    def test_check_skill1(self):
        #GIVEN
        character = Character(name='huross', 
                              level=5, race='elf', 
                              equipment='amulet', 
                              skill='arcana', 
                              username='jacky6')
        #WHEN
        check = character.check_skill()
        #THEN
        self.assertTrue(check)
    def test_check_skill2(self):
        #GIVEN
        character = Character(name='huross', 
                              level=5, race='elf', 
                              equipment='amulet', 
                              skill='this skill doesn\'t exist', 
                              username='jacky6')
        #WHEN
        check = character.check_skill()
        #THEN
        self.assertFalse(check)


if __name__ == '__main__':
    unittest.main()

    