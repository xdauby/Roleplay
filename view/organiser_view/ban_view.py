from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session


class BanView(AbstractView):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'input',
                'name': 'username',
                'message': 'Who\'s to ban',
            }
        ]

    def display_info(self):
        print("Ban section")

    def make_choice(self):
        
        reponse = prompt(self.__questions)

        #code to ban

        from view.organiser_view.menu_view import OrganiserMenuView
        return OrganiserMenuView()