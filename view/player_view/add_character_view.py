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
        from view.player_view.menu_view import PlayerMenuView

        if not str.isdigit(answers['level']) or answers['level'] =='' or answers['name'] =='' or answers['equipment'] =='' or answers['race'] =='' or answers['skill'] =='':
            print('Error : enter a number for level or fill all the blanks.')
            return PlayerMenuView()


        character_to_add = Character(name=answers['name']
                                    , level=answers['level']
                                    , race=answers['race']
                                    , equipment=answers['equipment']
                                    , skill=answers['skill']
                                    , username=Session().username) 
        
        print('Checking if race, equipment and skills are ok ...')
        if not character_to_add.check_race():
            print('This race is not in te game, please check the available races.')
            return PlayerMenuView()
        if not character_to_add.check_equipment():
            print('This equipment is not in the game, please check the available equipments.')
            return PlayerMenuView()
        if not character_to_add.check_skill():
            print('This skill is not in the game, please check the available skills.')
            return PlayerMenuView()

        if Session().player.basic_player.add_character(character_to_add):
            print('Character succesfully added')
        else:
            print('Something went wrong, probably you have to much characters.')
        
        return PlayerMenuView()
