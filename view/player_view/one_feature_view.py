from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session
from webservice.api_dd_v2 import ApiDungeonDragon


class OneFeatureView(AbstractView):

    def __init__(self):
        self.__questions = [
        
            {
                'type' : 'input',
                'name' : 'equipment',
                'message' : 'What equipments do you want a description of ?',
            },
            {
                'type' : 'input',
                'name' : 'race',
                'message' : 'What races do you want a description of ?',
            },
            {
                'type' : 'input',
                'name' : 'skills',
                'message' : 'What skills do you want a description of ?'
            }
        ]

    def display_info(self):
        print("")

    def make_choice(self) :
        answers = prompt(self.__questions)
        print(answers)
        description = ApiDungeonDragon().get_description(equipment = answers['equipment'], 
                                                            race = answers['race'], skills = answers['skills'])

        print(description)
        
        from view.player_view.menu_view import PlayerMenuView
        return PlayerMenuView()
        
        
        
        
        





