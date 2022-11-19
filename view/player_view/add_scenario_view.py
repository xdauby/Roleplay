from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session

from business.scenario.scenario import Scenario

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

        if answers['scenario_description']=='' or answers['scenario_name'] =='':
            print('Error : description or name must not be empty.')
            from view.player_view.menu_view import PlayerMenuView
            return PlayerMenuView()

        scenario_to_add = Scenario(name = answers['scenario_name']
                                    , description=answers['scenario_description']
                                    , username=Session().username)
        if Session().player.game_master.add_scenario(scenario_to_add):
            print('Scenario succesfully added')
        else:
            print('Something went wrong, probably you have to much scenarios.')
        
        from view.player_view.menu_view import PlayerMenuView
        return PlayerMenuView()
