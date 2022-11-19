from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session
from webservice.api_dd_v2 import ApiDungeonDragon


class OneFeatureView(AbstractView):

    def __init__(self):
        self.__questions = [
        
            {
                'type' : 'list',
                'name' : 'choice',
                'message' : 'From what type is the feature?',
                'choices' : [
                    'equipment'
                    , 'race'
                    , 'skill'
                ]
            },{
                'type' : 'input',
                'name' : 'feature',
                'message' : 'What the name of the feature you are you looking information on?'
            }
        ]

    def display_info(self):
        print("")

    def make_choice(self) :
        answers = prompt(self.__questions)

        if answers['choice'] == 'equipment' :
            description = ApiDungeonDragon().get_description(equipment = answers['feature'])
            if description['equipment']:
                print(description['equipment'])
            else:
                print('Unrecognised equipment')
        elif answers['choice'] == 'race' :
            description = ApiDungeonDragon().get_description(race = answers['feature'])
            if description['race']:
                print(description['race'])
            else:
                print('Unrecognised race')
        elif answers['choice'] == 'skill' :
            description = ApiDungeonDragon().get_description(skills = answers['feature'])
            if description['skills']:
                print(description['skills'])
            else:
                print('Unrecognised skill')

        
        
        from view.player_view.menu_view import PlayerMenuView
        return PlayerMenuView()
        
        
        
        
        





