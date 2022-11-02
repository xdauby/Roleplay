from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session

from business.character.character import Character

class AddCharacterView(AbstractView):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'input',
                'name': 'name',
                'message': 'What\'s the name of the Character ',
            },{
                'type': 'input',
                'name': 'level',
                'message': 'What\'s the character\'s level ',
            },{
                'type': 'input',
                'name': 'equipment',
                'message': 'What\'s the character\'s equipment ',
            },{
                'type': 'input',
                'name': 'race',
                'message': 'What\'s the character\'s race ',
            },{
                'type': 'input',
                'name': 'skill',
                'message': 'What\'s the character\'s skill ',
            }   
        ]

    def display_info(self):
        print("")

    def make_choice(self):
        answers = prompt(self.__questions)

        if not str.isdigit(answers['level']):
            print('Error : enter a number for level.')

        character_to_add = Character(name=answers['name']
                                    , level=answers['level']
                                    , race=answers['race']
                                    , equipment=answers['equipment']
                                    , skill=answers['skill']
                                    , username=Session().username) 
        
        if Session().player.basic_player.add_character(character_to_add):
            print('All is ok')
        else:
            print('pb somewhere')
        
        from view.player_view.menu_view import PlayerMenuView
        return PlayerMenuView()
