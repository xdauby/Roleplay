from PyInquirer import Separator, prompt

from view.abstract_view import AbstractView
from view.session import Session




class StartView(AbstractView):

    def __init__(self):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choice',
                'message': '',
                'choices': [
                    'Register as Player'
                    , 'Sign In as Player'
                    , 'Sign In as Organiser'
                    , 'Leave'
                ]
            }
        ]

    def display_info(self):
        print('')

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choice'] == 'Register as Player':
            from view.register_view import RegisterView
            return RegisterView()
        elif reponse['choice'] == 'Sign In as Player':
            from view.sign_in_view import SignInView
            return SignInView()
        elif reponse['choice'] == 'Sign In as Organiser':
            from view.sign_in_view import SignInView
            return SignInView()
        elif reponse['choice'] == 'Leave':
            return None
        
