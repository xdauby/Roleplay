from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session

class LeaveFromTableView(AbstractView):
    def __init__(self) -> None:

        if Session().user_type == 'player':
            self.__questions = [
                {
                    'type': 'input',
                    'name': 'table_id',
                    'message': 'What table you wanna leave?',
                }
            ]
        elif Session().user_type == 'organiser':
            self.__questions = [
                {
                    'type': 'input',
                    'name': 'username',
                    'message': 'Who is the player?',
                },
                {
                    'type': 'input',
                    'name': 'table_id',
                    'message': 'What table you wanna leave him from?',
                }
            ]


    def display_info(self):
        print("Leave Table Menu")

    def make_choice(self):
        answers = prompt(self.__questions)
        from business.table.table import Table
        

        if Session().user_type == 'player':

            table_to_leave = Table.load(int(answers['table_id']))
            
            if table_to_leave:
                if table_to_leave.rm_player(Session().username):
                    print('You\'ve been successfully removed from the table')
                else:
                    print('Something went wrong, may be you don\'t belong to this table')
            
            else:
                print("Unrocognised id table")

            from view.player_view.menu_view import PlayerMenuView
            return PlayerMenuView()

        elif Session().user_type == 'organiser':

            table_to_leave = Table.load(int(answers['table_id']))
            
            if table_to_leave:
                if table_to_leave.rm_player(answers['username']):
                    print('Player have been successfully removed from the table')
                    message = 'You\'ve been moved, check your tables !'
                    Session().organiser.notify_player(notif=message, username=answers['username'])

                else:
                    print('Something went wrong, may be you made a mistake on the username or the player don\'t belong to the table')
            else:
                print("Unrocognised id table")

            from view.organiser_view.menu_view import OrganiserMenuView
            return OrganiserMenuView()

