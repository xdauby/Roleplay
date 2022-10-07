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
        elif Session().user_type == 'oragniser':
            self.__questions = [
                {
                    'type': 'input',
                    'name': 'username',
                    'message': 'Who is the player?',
                },
                {
                    'type': 'input',
                    'name': 'table_id',
                    'message': 'What table you wanna leave?',
                }
            ]


    def display_info(self):
        print("You will leave a table.")

    def make_choice(self):
        answers = prompt(self.__questions)
        pprint(answers)


        if Session().user_type == 'player':
            #dao req
            from view.player_view.menu_view import PlayerMenuView
            return PlayerMenuView()

        elif Session().user_type == 'organiser':
            #dao req
            from view.organiser_view.menu_view import OrganiserMenuView
            return OrganiserMenuView()

