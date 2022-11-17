import unittest
from unittest import TestCase
from business.user.organiser import Organiser
from business.notification.notification import Notification
from dao.organiser_dao import OrganiserDao
from business.user.player import Player
from business.role.basic_player import BasicPlayer
from business.role.game_master import GameMaster

class TestOrganiserDao(TestCase):
    def test_load(self):

        #GIVEN
        expected_orga = Organiser(firstname='Natasha'
                                    , lastname='Duchar'
                                    , username='admin_orga2'
                                    , age=39
                                    , password='8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918')
        #WHEN
        orga_loaded = Organiser.load('admin_orga2')
        #THEN
        self.assertEqual(orga_loaded, expected_orga)
    
    def test_save_notif(self):

        #GIVEN        
        notif = Notification(notification= 'You have been moved, check your tables !'
                            , username= 'zrk')
        game_master = GameMaster(username='zrk')
        basic_player = BasicPlayer(username='zrk')
        player = Player(firstname='George'
                                , lastname='Grand'
                                , username='zrk'
                                , age=19
                                , game_master=game_master
                                , basic_player=basic_player
                                , password ='5cc55633769b725e714f9cdfc6c611e11e95bcb0f4f642ac922a373f0c91d055')

        player.save()
        #WHEN
        notifify = OrganiserDao().save_notif(notif)
        player_loaded = Player.load('zrk')
        #THEN
        self.assertTrue(notifify,)
        self.assertEqual(notif, player_loaded.notification)
        #free db
        Player.delete('zrk')

if __name__ == '__main__':
    #please, reinitialize the database before the test
    unittest.main()