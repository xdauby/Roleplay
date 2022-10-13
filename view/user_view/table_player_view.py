from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session

class TablePlayerView(AbstractView):
    
    def display_info(self):

        print("Your tables")
        
        if Session().user_type == 'player':
            Session().game_master.load_player_tables()
            Session().basic_player.load_player_tables()

        if Session().game_master.tables:
            for tables in Session().game_master.tables:
                print(tables)

        if Session().basic_player.tables:
            for tables in Session().basic_player.tables:
                print(tables)



        
    def make_choice(self):

        if Session().user_type == 'player':
            from view.player_view.menu_view import PlayerMenuView
            return PlayerMenuView()

        elif Session().user_type == 'organiser':
            from view.organiser_view.menu_view import OrganiserMenuView
            return OrganiserMenuView()