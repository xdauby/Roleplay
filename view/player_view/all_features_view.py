from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session
from webservice.api_dd_v2 import ApiDungeonDragon
from menu_view import PlayerMenuView

from business.scenario.scenario import Scenario

class AllFeaturesView(AbstractView):

    def display_info(self):
        print(ApiDungeonDragon.get_features_list())

    def make_choice(self):
        return PlayerMenuView()
