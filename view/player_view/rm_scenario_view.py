from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session


class RmScenarioView(AbstractView):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'input',
                'name': 'scenario_id',
                'message': 'What\'s the id of the Scenario to remove?',
            }
        ]

    def display_info(self):
        print("")

    def make_choice(self):
        answers = prompt(self.__questions)
        pprint(answers)
        scenario_id_to_del = int(answers['scenario_id'])

        if Session().game_master.rm_scenario(scenario_id_to_del):
            print(f'Scenario {scenario_id_to_del} succesfully deleted.')
        else:
            print('pb somwhere')
        
        from view.player_view.menu_view import PlayerMenuView
        return PlayerMenuView()
