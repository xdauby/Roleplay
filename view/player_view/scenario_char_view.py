from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session


class ScenCharView(AbstractView):
   
    def display_info(self):
        scenario = Session().game_master.scenarios
        character = Session().basic_player.characters
        if scenario:
            for scen in scenario:
                print(scen)
        if character:
            for char in character:
                print(char)


    def make_choice(self):
        from view.player_view.menu_view import PlayerMenuView
        return PlayerMenuView()
