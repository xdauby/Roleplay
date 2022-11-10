from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session
from webservice.api_dd_v2 import ApiDungeonDragon
from menu_view import PlayerMenuView

from business.scenario.scenario import Scenario


class OneFeatureView(AbstractView):

    def __init__(self):
        self.__questions = [
            {
                'type' : 'input',
                'name' : 'feature',
                'message' : 'What feature are you looking information on?'
            },
            {
                'type' : 'choice',
                'name' : 'type_feature',
                'message' : 'from what type is the feature?',
                'choices' : [
                    'equipment'
                    , 'race'
                    , 'skill'
                ]
            }
        ]

    def display_info(self):
        print("")

    def make_choice(self) :
        answers = prompt(self.__questions)

        if answers['choices'] == 'equipment' :
            description = ApiDungeonDragon.get_descriptions(equipment = answers['feature'])
        
        elif answers['choices'] == 'race' :
            description = ApiDungeonDragon.get_descriptions(race = answers['feature'])

        elif answers['choices'] == 'skill' :
            description = ApiDungeonDragon.get_descriptions(skills = answers['feature'])

        print(description)

        return PlayerMenuView()
    

        
        
        
        
        





