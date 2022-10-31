import unittest
from unittest import TestCase
from business.table.table import Table
from business.role.game_master import GameMaster
from business.role.basic_player import BasicPlayer
from business.user.player import Player
from business.scenario.scenario import Scenario
from business.character.character import Character
class TestTable(TestCase):

    def test_add_gamemaster_case1(self):
        #case1 : empty table
        #GIVEN
        player = Player(firstname='Jean'
                        , lastname='Hill'
                        , username='ninho'
                        , age=9
                        , game_master=GameMaster(username='ninho')
                        , basic_player=BasicPlayer(username='ninho'))
        player.save()
        scenario1 = Scenario(name='test'
                            , description='this is a test'
                            , username='ninho')
        player.game_master.add_scenario(scenario1)
        id_scenario = scenario1.id
        #table 7 must be empty and active in the db for the test
        table = Table(half_day=1, active = True, id=7)
        #WHEN
        added = table.add_gamemaster(player, id_scenario)
        #THEN  
        self.assertTrue(added)

    def test_add_gamemaster_case2(self):
        #case2 : table has already a gamemaster
        #GIVEN
        player1 = Player(firstname='Jean'
                        , lastname='Hill'
                        , username='jacky1'
                        , age=9
                        , game_master=GameMaster(username='jacky1')
                        , basic_player=BasicPlayer(username='jacky1'))

        player2 = Player(firstname='Jean'
                        , lastname='Hill'
                        , username='jacky2'
                        , age=9
                        , game_master=GameMaster(username='jacky2')
                        , basic_player=BasicPlayer(username='jacky2'))
        player1.save()
        player2.save()

        scenario1p1 = Scenario(name='test'
                            , description='this is a test'
                            , username='jacky1')

        scenario1p2 = Scenario(name='test'
                            , description='this is a test'
                            , username='jacky2')
        
        player1.game_master.add_scenario(scenario1p1)
        player2.game_master.add_scenario(scenario1p2)

        table = Table(half_day=1, active = True, id=8)
        table.add_gamemaster(player1, scenario1p1.id)
        
        #WHEN
        added = table.add_gamemaster(player2, scenario1p2.id)
        
        #THEN  
        self.assertFalse(added)

    def test_add_gamemaster_case3(self):
        #case3 : player is registered the same halfday
        #GIVEN

        player = Player(firstname='Jean'
                        , lastname='Hill'
                        , username='jacky3'
                        , age=9
                        , game_master=GameMaster(username='jacky3')
                        , basic_player=BasicPlayer(username='jacky3'))

        player.save()

        scenario1 = Scenario(name='test'
                            , description='this is a test'
                            , username='jacky3')
        player.game_master.add_scenario(scenario1)

        #table 8 and 9 must be empty and active in the db for the test :
        #by default, they are.
        table1 = Table(half_day=1, active = True, id=8)
        table2 = Table(half_day=1, active = True, id=9)

        table1.add_gamemaster(player, scenario1.id)

        #WHEN
        added = table2.add_gamemaster(player, scenario1.id)
        #THEN  
        self.assertFalse(added)

    def test_add_basic_player_case1(self):
        #case1 : empty table
        #must be false because a player can join a table only if there is a game master
        #GIVEN
        player = Player(firstname='Jean'
                        , lastname='Hill'
                        , username='jacky4'
                        , age=9
                        , game_master=GameMaster(username='jacky4')
                        , basic_player=BasicPlayer(username='jacky4'))

        player.save()        

        character1 = Character(name='huross', 
                              level=5, race='bard', 
                              equipment='amulet', 
                              skill='battleaxes', 
                              username='jacky4')

        player.basic_player.add_character(character1)
        #table 9 must be empty and active in the db for the test : by default, it is.
        table = Table(half_day=1, active = True, id=9)
        #WHEN
        added = table.add_basicplayer(player, character1.id)
        #THEN  
        self.assertFalse(added)

    def test_add_basic_player_case2(self):
        #case2 : player registered the same halfday
        #GIVEN
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

        scenario1p3 = Scenario(name='test2'
                            , description='this is a test'
                            , username='jacky7')

        character1p2 = Character(name='huross', 
                              level=5, race='bard', 
                              equipment='amulet', 
                              skill='battleaxes', 
                              username='jacky6')
        character2p2 = Character(name='hugobosss', 
                              level=5, race='bard', 
                              equipment='amulet', 
                              skill='battleaxes', 
                              username='jacky6')
        
        player1.game_master.add_scenario(scenario1p1)    

        player2.basic_player.add_character(character1p2)
        player2.basic_player.add_character(character2p2)

        #tables 23 and 24 must be empty and active in the db for the test : by default, it is.
        table1 = Table(half_day=2, active = True, id=23)
        table2 = Table(half_day=2, active = True, id=24)

        table1.add_gamemaster(player1, scenario1p1.id)
        table1.add_basicplayer(player2, character1p2.id)
        table2.add_gamemaster(player3, scenario1p3.id) 
        
        #WHEN
        added = table2.add_basicplayer(player2, character2p2.id)
        #THEN  
        self.assertFalse(added)

    
    def test_add_basic_player_case3(self):
        #case 3: the number of basic player is 4
        #GIVEN




        player1 = Player(firstname='Jean'
                        , lastname='Hill'
                        , username='jacky8'
                        , age=9
                        , game_master=GameMaster(username='jacky8')
                        , basic_player=BasicPlayer(username='jacky8'))

        player2 = Player(firstname='Jean'
                        , lastname='Hill'
                        , username='jacky9'
                        , age=9
                        , game_master=GameMaster(username='jacky9')
                        , basic_player=BasicPlayer(username='jacky9'))
        
        player3 = Player(firstname='Jean'
                        , lastname='Hill'
                        , username='jacky10'
                        , age=9
                        , game_master=GameMaster(username='jacky10')
                        , basic_player=BasicPlayer(username='jacky10'))
        
        player4 = Player(firstname='Jean'
                        , lastname='Hill'
                        , username='jacky11'
                        , age=9
                        , game_master=GameMaster(username='jacky11')
                        , basic_player=BasicPlayer(username='jacky11'))

        player5 = Player(firstname='Jean'
                        , lastname='Hill'
                        , username='jacky12'
                        , age=9
                        , game_master=GameMaster(username='jacky12')
                        , basic_player=BasicPlayer(username='jacky12'))

        player6 = Player(firstname='Jean'
                        , lastname='Hill'
                        , username='jacky13'
                        , age=9
                        , game_master=GameMaster(username='jacky13')
                        , basic_player=BasicPlayer(username='jacky13'))
        
        player1.save()
        player2.save()
        player3.save()
        player4.save()
        player5.save()      

        scenario1p1 = Scenario(name='test'
                            , description='this is a test'
                            , username='jacky8')

    
        character1p2 = Character(name='huross1', 
                              level=5, race='bard', 
                              equipment='amulet', 
                              skill='battleaxes', 
                              username='jacky9')

        character1p3 = Character(name='huross2', 
                              level=5, race='bard', 
                              equipment='amulet', 
                              skill='battleaxes', 
                              username='jacky10')

        character1p4 = Character(name='huross3', 
                              level=5, race='bard', 
                              equipment='amulet', 
                              skill='battleaxes', 
                              username='jacky11')

        character1p5 = Character(name='huross4', 
                              level=5, race='bard', 
                              equipment='amulet', 
                              skill='battleaxes', 
                              username='jacky12')

        character1p6 = Character(name='huross5', 
                              level=5, race='bard', 
                              equipment='amulet', 
                              skill='battleaxes', 
                              username='jacky13')              

        table = Table(half_day=2, active = True, id=25)                              
        table.add_gamemaster(player1, scenario1p1.id)
        table.add_basicplayer(player2, character1p2.id)
        table.add_basicplayer(player3, character1p3.id)
        table.add_basicplayer(player4, character1p4.id)
        table.add_basicplayer(player5, character1p5.id)

        #WHEN
        added = table.add_basicplayer(player2, character1p6.id)

        #THEN  
        self.assertFalse(added)
        pass

    def test_add_basic_player_case4(self):
        #case 4: the player can be added
        #GIVEN

        player1 = Player(firstname='Jean'
                        , lastname='Hill'
                        , username='jacky14'
                        , age=9
                        , game_master=GameMaster(username='jacky14')
                        , basic_player=BasicPlayer(username='jacky14'))

        player2 = Player(firstname='Jean'
                        , lastname='Hill'
                        , username='jacky15'
                        , age=9
                        , game_master=GameMaster(username='jacky15')
                        , basic_player=BasicPlayer(username='jacky15'))
        
        
        player1.save()
        player2.save()

        scenario1p1 = Scenario(name='test'
                            , description='this is a test'
                            , username='jacky14')


        character1p2 = Character(name='huross', 
                              level=5, race='bard', 
                              equipment='amulet', 
                              skill='battleaxes', 
                              username='jacky15')
        
        player1.game_master.add_scenario(scenario1p1)    
        player2.basic_player.add_character(character1p2)

        #tables 26 must be empty and active in the db for the test : by default, it is.
        table = Table(half_day=2, active = True, id=26)
        table.add_gamemaster(player1, scenario1p1.id)
        #WHEN
        added = table.add_basicplayer(player2, character1p2.id)
        #THEN  
        self.assertTrue(added)

    def test_rm_player_case1(self):
        #case1 : the user is not in the table
        #GIVEN

        player1 = Player(firstname='Jean'
                        , lastname='Hill'
                        , username='jacky16'
                        , age=9
                        , game_master=GameMaster(username='jacky16')
                        , basic_player=BasicPlayer(username='jacky16'))

        player2 = Player(firstname='Jean'
                        , lastname='Hill'
                        , username='jacky17'
                        , age=9
                        , game_master=GameMaster(username='jacky17')
                        , basic_player=BasicPlayer(username='jacky17'))
        
        
        player1.save()
        player2.save()

        scenario1p1 = Scenario(name='test'
                            , description='this is a test'
                            , username='jacky16')


        character1p2 = Character(name='huross', 
                              level=5, race='bard', 
                              equipment='amulet', 
                              skill='battleaxes', 
                              username='jacky17')
        
        player1.game_master.add_scenario(scenario1p1)    
        player2.basic_player.add_character(character1p2)

        #tables 27 must be empty and active in the db for the test : by default, it is.
        table = Table(half_day=2, active = True, id=27)
        table.add_gamemaster(player1, scenario1p1.id)
        table.add_basicplayer(player2, character1p2.id)
        username = 'jojokiki2'
        #WHEN
        removed = table.rm_player(username)
        #THEN
        self.assertFalse(removed)
    
    def test_rm_player_case2(self):
        #case2 : delete a basic player
        #GIVEN

        player1 = Player(firstname='Jean'
                        , lastname='Hill'
                        , username='jacky18'
                        , age=9
                        , game_master=GameMaster(username='jacky18')
                        , basic_player=BasicPlayer(username='jacky18'))

        player2 = Player(firstname='Jean'
                        , lastname='Hill'
                        , username='jacky19'
                        , age=9
                        , game_master=GameMaster(username='jacky19')
                        , basic_player=BasicPlayer(username='jacky19'))
        
        
        player1.save()
        player2.save()

        scenario1p1 = Scenario(name='test'
                            , description='this is a test'
                            , username='jacky18')


        character1p2 = Character(name='huross', 
                              level=5, race='bard', 
                              equipment='amulet', 
                              skill='battleaxes', 
                              username='jacky19')
        
        player1.game_master.add_scenario(scenario1p1)    
        player2.basic_player.add_character(character1p2)

        #tables 28 must be empty and active in the db for the test : by default, it is.
        table = Table(half_day=2, active = True, id=28)
        table.add_gamemaster(player1, scenario1p1.id)
        table.add_basicplayer(player2, character1p2.id)
        username = 'jacky19' #the basic player
        #WHEN
        removed = table.rm_player(username)
        #THEN
        self.assertTrue(removed)

    def test_rm_player_case2(self):
        #case3 : delete a game master
        #GIVEN

        player1 = Player(firstname='Jean'
                        , lastname='Hill'
                        , username='jacky20'
                        , age=9
                        , game_master=GameMaster(username='jacky20')
                        , basic_player=BasicPlayer(username='jacky20'))

        player2 = Player(firstname='Jean'
                        , lastname='Hill'
                        , username='jacky21'
                        , age=9
                        , game_master=GameMaster(username='jacky21')
                        , basic_player=BasicPlayer(username='jacky21'))
        
        
        player1.save()
        player2.save()

        scenario1p1 = Scenario(name='test'
                            , description='this is a test'
                            , username='jacky20')


        character1p2 = Character(name='huross', 
                              level=5, race='bard', 
                              equipment='amulet', 
                              skill='battleaxes', 
                              username='jacky21')
        
        player1.game_master.add_scenario(scenario1p1)    
        player2.basic_player.add_character(character1p2)

        #tables 29 must be empty and active in the db for the test : by default, it is.
        table = Table(half_day=2, active = True, id=29)
        table.add_gamemaster(player1, scenario1p1.id)
        table.add_basicplayer(player2, character1p2.id)
        username = 'jacky20' #the basic player
        #WHEN
        removed = table.rm_player(username)
        #THEN
        self.assertTrue(removed) 

    def test_activate_table(self):
        #GIVEN
        #tables 33 must be empty and desactivated in the db for the test : by default, it is.
        table = Table(halfday = 2, active = False, id = 33)
        #WHEN
        table.active_table()
        #then
        self.assertTrue(table.active)

    def test_desactive_table_case1(self):
        #case1 : table is empty
        #GIVEN
        #tables 44 must be empty and activated in the db for the test : by default, it is.
        table = Table(halfday = 3, active = True, id = 44)
        #WHEN
        table.desactive_table()
        #then
        self.assertFalse(table.active)
    
    def test_desactive_table_case1(self):
        #case2 : the table is not empty
        #tables 45 must be empty and activated in the db for the test : by default, it is.
    
        pass

if __name__ == '__main__':
    #please, reinitialize the database before the test
    unittest.main()
    


