from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session
from webservice.api_dd_v2 import ApiDungeonDragon

from business.scenario.scenario import Scenario

class AllFeaturesView(AbstractView):

    def display_info(self):
        print('Waiting for feature ...')
        features = ApiDungeonDragon().get_features_list()
        equipments = features['equipments']
        skills = features['skills']
        races = features['races']

        print('\nEquipments : \n')
        for equipment in equipments:
            print(f'    {equipment}')
        print('\nRaces : \n')
        for race in races:
            print(f'    {race}')
        print('\nSkills : \n')
        for skill in skills:
            print(f'    {skill}')

    def make_choice(self):
        from view.player_view.menu_view import PlayerMenuView
        return PlayerMenuView()
