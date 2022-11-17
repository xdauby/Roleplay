from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session

from business.user.player import Player

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
                    , 'display all features for characters'
                    , 'display description of a feature '
                    , 'Leave'
                ]
            }
        ]

    def display_info(self):
        
        notif = Session().player.notification
        if notif:
            print(notif)
            Session().player.delete_notif()

        print(f'{Session().username}, choose an action.')

    def make_choice(self):
        reponse = prompt(self.__questions)
        
        #actualisation
        Session().player = Player.load(Session().username)

  
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
            from view.player_view.add_character_view import AddCharacterView
            return AddCharacterView()

        elif reponse['choice'] == 'remove character':
            from view.player_view.rm_character_view import RmCharacterView
            return RmCharacterView()

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

        elif reponse['choice'] == 'display all features for characters':
            from view.player_view.all_features_view import AllFeaturesView
            return AllFeaturesView()

        elif reponse['choice'] == 'display description of a feature ':
            from view.player_view.one_feature_view import OneFeatureView
            return OneFeatureView()

        elif reponse['choice'] == 'Leave':
            return None