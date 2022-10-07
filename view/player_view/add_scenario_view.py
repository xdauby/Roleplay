from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session


class AddScenarioView(AbstractView):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'input',
                'name': 'scenario_name',
                'message': 'What\'s the name of the Scenario ',
            },{
                'type': 'input',
                'name': 'scenario_description',
                'message': 'What\'s the description ',
            }
        ]

    def display_info(self):
        print("")

    def make_choice(self):
        answers = prompt(self.__questions)
        pprint(answers)
        if True:
            from view.player_view.menu_view import PlayerMenuView
            return PlayerMenuView()
