from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session


class RmCharacterView(AbstractView):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'input',
                'name': 'character_id',
                'message': 'What\'s the id of the Character to remove?',
            }
        ]

    def display_info(self):
        print("")

    def make_choice(self):
        answers = prompt(self.__questions)

        character_id_to_del = int(answers['character_id'])

        if Session().player.basic_player.rm_character(character_id_to_del):
            print(f'Character id : {character_id_to_del} succesfully deleted.')
        else:
            print('Something went wrong, maybe it\'s not the good id.')
        
        from view.player_view.menu_view import PlayerMenuView
        return PlayerMenuView()
