from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session
from webservice.service_dd import ServiceDD


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

        description = ServiceDD().get_description(equipment = answers['equipment'], 
                                                            race = answers['race'], skills = answers['skills'])

        if description['equipment']:
            print(f"{answers['equipment']} : {description['equipment']}")
        else:
            print('Unrecognised equipment')
        
        if description['race']:
            print(f"{answers['race']} : {description['race']}")
        else:
            print('Unrecognised race')
        
        if description['skills']:
            print(f"{answers['skills']} : {description['skills']}")
        else:
            print('Unrecognised skill')
        
        from view.player_view.menu_view import PlayerMenuView
        return PlayerMenuView()
        
        
        
        
        





