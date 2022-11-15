from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session
from business.table.table import Table


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
            
            tables = Table.load_player_tables(id_list_table = Session().player.tables)

            if tables:
                for table in tables:
                    print(table)


            from view.player_view.menu_view import PlayerMenuView
            return PlayerMenuView()

        if Session().user_type == 'organiser':
            answers = prompt(self.__questions)

            from business.user.player import Player

            player = Player.load(answers['username'])
            
            if player:
                tables = Table.load_player_tables(id_list_table = player.tables)
                if tables:
                    for table in tables:
                        print(table)
            else:
                print('The player does\'t exist')

            from view.organiser_view.menu_view import OrganiserMenuView
            return OrganiserMenuView()

        