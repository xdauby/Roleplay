from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session


class AddTableView(AbstractView):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'input',
                'name': 'table_id',
                'message': 'Table to add, please enter the id.',
            }
        ]

    def display_info(self):
        print("Add table Section")

    def make_choice(self):
        
        answers = prompt(self.__questions)

        if not str.isdigit(answers['table_id']) or answers['table_id'] == '':
            print('Error : table id must be a number.')
            
        else:

            from business.table.table import Table
            table = Table.load(answers['table_id'])
            if table:
                if table.active_table():
                    print('Table successfully activated')
                else:
                    print('Something went wrong when you tried to desactivate the table.')
            else:
                print('Table id unrocognised.')
        
        from view.organiser_view.menu_view import OrganiserMenuView
        return OrganiserMenuView()