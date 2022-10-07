from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session


class RmTableView(AbstractView):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'input',
                'name': 'id',
                'message': 'Table to remove, please enter the id.',
            }
        ]

    def display_info(self):
        print("Remove table Section")

    def make_choice(self):
        
        reponse = prompt(self.__questions)
        #code to add table
        
        from view.organiser_view.menu_view import OrganiserMenuView
        return OrganiserMenuView()