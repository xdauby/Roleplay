from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session

from business.user.basic_player import BasicPlayer
from business.user.game_master import GameMaster
from business.user.organiser import Organiser



class SignInView(AbstractView):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'input',
                'name': 'username',
                'message': 'What\'s your username',
            }
        ]

    def display_info(self):
        print("Hello, please sign in.")

    def make_choice(self):
        
        answers = prompt(self.__questions)
        pprint(answers)

        Session().username = None
        Session().basic_player = BasicPlayer.load(answers['username'])
        Session().game_master = GameMaster.load(answers['username'])
        Session().organiser = Organiser.load(answers['username'])


        if Session().basic_player or Session().game_master:
            Session().user_type = 'player'
            Session().username = answers['username']
            from view.player_view.menu_view import PlayerMenuView
            return PlayerMenuView()
        
        if Session().organiser:
            Session().user_type = 'organiser'
            Session().username = answers['username']
            from view.organiser_view.menu_view import OrganiserMenuView
            return OrganiserMenuView()
        else:
            print('User unrecognised')
            from view.start_view import StartView
            return StartView()