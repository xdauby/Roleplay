from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session


class RmTableView(AbstractView):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'input',
                'name': 'table_id',
                'message': 'Table to remove, please enter the id.',
            }
        ]

    def display_info(self):
        print("Remove table Section")

    def make_choice(self):
        
        answers = prompt(self.__questions)


        if not str.isdigit(answers['table_id']):
            print('Error : table id must be a number.')
        else:
            from business.table.table import Table
            table = Table.load(answers['table_id'])
            if table:
                if table.desactive_table():
                    message = 'You\'ve been moved, check your tables !'
                    for player in table.players:
                        Session().organiser.notify_player(notif=message, username=player.username)

                    print('Table successfully desactivated')
                else:
                    print('Something went wrong when you tried to desactivate the table.')
            else:
                print('Table id unrocognised.')

        from view.organiser_view.menu_view import OrganiserMenuView
        return OrganiserMenuView()