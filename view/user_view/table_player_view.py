from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session

class TablePlayerView(AbstractView):
    
    def __init__(self) -> None:

        if Session().user_type == 'organiser':
            self.__questions = [
                {
                    'type': 'input',
                    'name': 'username',
                    'message': 'Who\'s the player you want to look tables?',
                }
            ]
    
    def display_info(self):
        print("Tables : ")
        
        
    def make_choice(self):

        if Session().user_type == 'player':
            
            tables_gm = Session().player.game_master.load_player_tables()
            tables_bp = Session().player.basic_player.load_player_tables()

            if tables_gm:
                for tables in tables_gm:
                    print(tables)

            if tables_bp:
                for tables in tables_bp:
                    print(tables)
            from view.player_view.menu_view import PlayerMenuView
            return PlayerMenuView()

        if Session().user_type == 'organiser':
            answers = prompt(self.__questions)

            from business.user.player import Player

            player = Player.load(answers['username'])
            
            if player:

                tables_gm = player.game_master.load_player_tables()
                tables_bp = player.basic_player.load_player_tables()

                if tables_gm:
                    for tables in tables_gm:
                        print(tables)

                if tables_bp:
                    for tables in tables_bp:
                        print(tables)
            else:
                print('The player does\'t exist')

            from view.organiser_view.menu_view import OrganiserMenuView
            return OrganiserMenuView()

        