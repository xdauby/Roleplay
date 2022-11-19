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
        from view.player_view.menu_view import PlayerMenuView


        if not str.isdigit(answers['character_id']) or answers['character_id']=='':
                print('Error : Id must be an integer.')
                return PlayerMenuView()

        character_id_to_del = int(answers['character_id'])


        if Session().player.basic_player.rm_character(character_id_to_del):
            print(f'Character id : {character_id_to_del} succesfully deleted.')
        else:
            print('Something went wrong, maybe it\'s not the good id.')
        
        return PlayerMenuView()
