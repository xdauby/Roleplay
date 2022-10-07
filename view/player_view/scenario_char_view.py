from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session


class ScenCharView(AbstractView):
   
    def display_info(self):
        print("Hello")

    def make_choice(self):
        from view.player_view.menu_view import PlayerMenuView
        return PlayerMenuView()
