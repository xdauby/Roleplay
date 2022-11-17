import unittest
from unittest import TestCase
from business.scenario.scenario import Scenario


class TestScenario(TestCase):

    def test_str(self):
        #GIVEN
        scenario = Scenario('test', 'this is a test')
        #WHEN
        string = scenario.__str__()
        #THEN  
        self.assertEqual('Scenario \n Id : None \n Name : test \n Description : this is a test', string)


if __name__ == '__main__':
    unittest.main()



