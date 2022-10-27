from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session
from business.user.abstract_player import Player

class RegisterView(AbstractView):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'input',
                'name': 'username',
                'message': 'What\'s your username',
            },
            {
                'type': 'input',
                'name': 'firstname',
                'message': 'What\'s your first name',
            },
            {
                'type': 'input',
                'name': 'lastname',
                'message': 'What\'s your last name',
            },
            {
                'type': 'input',
                'name': 'age',
                'message': 'What\'s your age',
            }

            
        ]

    def display_info(self):
        print("Hello, please register.")

    def make_choice(self):
        answers = prompt(self.__questions)


        if not str.isdigit(answers['age']):
            print('Error : Your age is not a number.')
            from view.start_view import StartView
            return StartView()

        player = Player.load(answers['username'])
        if player:
            print('Player already registered with this username, please try another')
            from view.start_view import StartView
            return StartView()
        else:
            player = Player( answers['firstname'], answers['lastname'], answers['username'], answers['age'])
            player.save()
            Session().user_type = 'player'
            Session().username = answers['username']
            from view.player_view.menu_view import PlayerMenuView
            return PlayerMenuView()
        
        
        
