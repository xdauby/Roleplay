from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session

class OrganiserMenuView(AbstractView):
    
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'list',
                'name': 'choice',
                'message': '',
                'choices': [
                    'add player table'
                    , 'remove player table'
                    , 'ban player'
                    , 'add table'
                    , 'remove table'
                    , 'display player tables'
                    , 'display all tables'
                    , 'Leave'
                ]
            }
        ]

    def display_info(self):
        print('')

    def make_choice(self):
        reponse = prompt(self.__questions)
        
        if reponse['choice'] == 'add player table':
            from view.user_view.add_to_table_view import AddToTableView
            return AddToTableView()
        elif reponse['choice'] == 'remove player table':
            return
        elif reponse['choice'] == 'ban player':
            from view.organiser_view.ban_view import BanView
            return BanView()
        elif reponse['choice'] == 'add table':
            from view.organiser_view.add_table_view import AddTableView
            return AddTableView()
        elif reponse['choice'] == 'remove table':
            from view.organiser_view.rm_table_view import RmTableView
            return RmTableView()
        elif reponse['choice'] == 'display player tables':
            from view.user_view.table_player_view import TablePlayerView
            return TablePlayerView()
        elif reponse['choice'] == 'display all tables':
            from view.user_view.table_view import TableView
            return TableView()
        elif reponse['choice'] == 'Leave':
            return None