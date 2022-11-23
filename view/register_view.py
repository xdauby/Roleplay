from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session
from business.user.player import Player
from business.notification.notification import Notification
from utils_.hash import hash_password

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
            },
            {
                'type': 'input',
                'name': 'pw',
                'message': 'What\'s your password',
            }
            
        ]

    def display_info(self):
        print("Hello, please register.")

    def make_choice(self):
        answers = prompt(self.__questions)


        if not str.isdigit(answers['age']) or answers['age']=='' or answers['username']=='' or answers['firstname']=='' or answers['lastname']=='':
            print('Error : Your age is not a number or you must fill in all the blanks.')
            from view.start_view import StartView
            return StartView()

        player = Player.load(answers['username'])
        
        if player:
            print('Player already registered with this username, please try another')
            from view.start_view import StartView
            return StartView()
        else:
            password = hash_password(answers['pw'])
            player = Player(firstname=answers['firstname']
                            , lastname=answers['lastname']
                            , username=answers['username']
                            , age=answers['age']
                            , password=password)
            player.save()
            player.notification = Notification(notification='Welcome !', username=answers['username'])
            
            Session().player = player

            Session().user_type = 'player'
            Session().username = answers['username']
            from view.player_view.menu_view import PlayerMenuView
            return PlayerMenuView()
        
        
        
