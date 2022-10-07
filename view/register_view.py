from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session


class RegisterView(AbstractView):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'input',
                'name': 'first_name',
                'message': 'What\'s your first name',
            },
            {
                'type': 'input',
                'name': 'last_name',
                'message': 'What\'s your last name',
            },
            {
                'type': 'input',
                'name': 'username',
                'message': 'What\'s your username',
            }
        ]

    def display_info(self):
        print("Hello, please register.")

    def make_choice(self):
        answers = prompt(self.__questions)
        pprint(answers)
        from view.start_view import StartView
        return StartView()
