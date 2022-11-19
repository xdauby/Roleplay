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
        from view.player_view.menu_view import PlayerMenuView

        answers = prompt(self.__questions)

        if not str.isdigit(answers['scenario_id']) or answers['scenario_id']=='':
                print('Error : Id must be an integer.')
                return PlayerMenuView()

        scenario_id_to_del = int(answers['scenario_id'])

        if Session().player.game_master.rm_scenario(scenario_id_to_del):
            print(f'Scenario id : {scenario_id_to_del} succesfully deleted.')
        else:
            print('Something went wrong, maybe it\'s not the good id.')
        
        return PlayerMenuView()
