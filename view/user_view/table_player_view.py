from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session



class TablePlayerView(AbstractView):
    
    def display_info(self):

        print("Voici vos tables les tables")
        
    def make_choice(self):

        if Session().user_type == 'player':
            from view.player_view.menu_view import PlayerMenuView
            return PlayerMenuView()

        elif Session().user_type == 'organiser':
            from view.organiser_view.menu_view import OrganiserMenuView
            return OrganiserMenuView()