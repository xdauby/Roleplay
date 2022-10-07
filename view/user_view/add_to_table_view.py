from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session


class AddToTableView(AbstractView):
    def __init__(self) -> None:
        
        if Session().user_type == 'player':
            self.__questions = [
                {
                    'type': 'input',
                    'name': 'table_id',
                    'message': 'What table you wanna join?',
                },{
                    'type': 'list',
                    'name': 'role',
                    'message': '',
                    'choices': [
                        'Game Master'
                        , 'Basic Player'
                    ]
                },
                {
                    'type': 'list',
                    'name': 'scenchar',
                    'message': '',
                    'choices': self.get_scenario_or_character
                }
            ]
        
        elif Session().user_type == 'organiser':
            self.__questions = [
                {
                    'type': 'input',
                    'name': 'table_id',
                    'message': 'What table you want to add the player to?',
                },{
                    'type': 'list',
                    'name': 'role',
                    'message': 'The player will be game master or basic player',
                    'choices': [
                        'Game Master'
                        , 'Basic Player'
                    ]
                },
                {
                    'type': 'list',
                    'name': 'scenchar',
                    'message': '',
                    'choices': self.get_scenario_or_character
                }
            ]


    def display_info(self):
        print("Hello")

    def get_scenario_or_character(self, answer):
        #fetch data on database
        scenario = ['scen1', 'scen2']
        chara = ['Boby']
        if answer['role'] == 'Game Master':
            return scenario
        else:
            return chara 


    def make_choice(self):
        answers = prompt(self.__questions)
        pprint(answers)

        if Session().user_type == 'player':
            from view.player_view.menu_view import PlayerMenuView
            return PlayerMenuView()

        elif Session().user_type == 'organiser':
            from view.organiser_view.menu_view import OrganiserMenuView
            return OrganiserMenuView()
