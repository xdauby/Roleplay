from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session

class PlayerMenuView(AbstractView):
    
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'list',
                'name': 'choice',
                'message': '',
                'choices': [
                    'Join table'
                    , 'Leave table'
                    , 'display my scenarios and characters'
                    , 'add character'
                    , 'remove character'
                    , 'add scenario'
                    , 'remove scenario'
                    , 'display my tables'
                    , 'display all tables'
                    , 'Leave'
                ]
            }
        ]

    def display_info(self):
        print(f'{Session().username}, choose an action.')

    def make_choice(self):
        reponse = prompt(self.__questions)
        
        if reponse['choice'] == 'Join table':
            from view.user_view.add_to_table_view import AddToTableView
            return AddToTableView()

        elif reponse['choice'] == 'Leave table':
            from view.user_view.leave_from_table_view import LeaveFromTableView
            return LeaveFromTableView()

        elif reponse['choice'] == 'display my scenarios and characters':
            from view.player_view.scenario_char_view import ScenCharView
            return ScenCharView()

        elif reponse['choice'] == 'add character':
            return

        elif reponse['choice'] == 'remove character':
            return

        elif reponse['choice'] == 'add scenario':
            from view.player_view.add_scenario_view import AddScenarioView
            return AddScenarioView()

        elif reponse['choice'] == 'remove scenario':
            from view.player_view.rm_scenario_view import RmScenarioView
            return RmScenarioView()
            
        elif reponse['choice'] == 'display my tables':
            from view.user_view.table_player_view import TablePlayerView
            return TablePlayerView()
        elif reponse['choice'] == 'display all tables':
            from view.user_view.table_view import TableView
            return TableView()
        elif reponse['choice'] == 'Leave':
            return None