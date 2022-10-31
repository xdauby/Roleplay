from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session

class AddToTableView(AbstractView):
    def __init__(self) -> None:
        self.temp_characters = []
        self.temp_scenarios = []
        if Session().user_type == 'player':
            self.__questions = [
                {
                    'type': 'input',
                    'name': 'table_id',
                    'message': 'What table you wanna join?',
                },{
                    'type': 'list',
                    'name': 'role',
                    'message': '',
                    'choices': [
                        'Game Master'
                        , 'Basic Player'
                    ]
                },
                {
                    'type': 'list',
                    'name': 'scenchar',
                    'message': '',
                    'choices': self.get_scenario_or_character
                }
            ]
        
        elif Session().user_type == 'organiser':
            self.__questions = [
                {
                    'type': 'input',
                    'name': 'username',
                    'message': 'Who\'s player you want to add?',
                },{
                    'type': 'input',
                    'name': 'table_id',
                    'message': 'What table you want to add the player to?',
                },{
                    'type': 'list',
                    'name': 'role',
                    'message': 'The player will be game master or basic player',
                    'choices': [
                        'Game Master'
                        , 'Basic Player'
                    ]
                },
                {
                    'type': 'list',
                    'name': 'scenchar',
                    'message': '',
                    'choices': self.get_scenario_or_character
                }
            ]
            
             
            


    def display_info(self):
        print("")

    def get_scenario_or_character(self, answer):
        
        if Session().user_type == 'organiser':
            from business.user.player import Player
        
            player = Player.load(answer['username'])

            if player:

                self.player = player                
                self.gm = player.game_master
                self.bp = player.basic_player

                scenarios = self.gm.scenarios
                characters = self.bp.characters

            else:
                error_message = ['Error : No player with this username, press to join the menu.']
                return error_message

        elif Session().user_type == 'player':
            scenarios = Session().player.game_master.scenarios
            characters = Session().player.basic_player.characters
        
        
        scenario_id = [str(scenario.id) for scenario in scenarios]
        character_id = [str(character.id) for character in characters]

        if answer['role'] == 'Game Master':
            if scenario_id == []:
                scenario_id = ['Error : You don\'t have any scenario, press to join the menu.']
            return scenario_id
        else:
            if character_id == []:
                character_id = ['Error : You don\'t have any character, press to join the menu.']
            return character_id 

    
    def make_choice(self):
        answers = prompt(self.__questions)

        if Session().user_type == 'player':
            from view.player_view.menu_view import PlayerMenuView
            
            if answers['scenchar'][0:5] == 'Error':
                return PlayerMenuView()
            
            from business.table.table import Table
            if answers['role'] == 'Game Master':
                id_scenario = int(answers['scenchar'])
                table = Table.load(answers['table_id'])
                if table:
                    if table.add_gamemaster(Session().player, id_scenario):
                        print('Successfully added to the table.')
                    else:
                        print('Something went wrong when you tried to join the table')
                else:
                    print('Table not found.')

            if answers['role'] == 'Basic Player':
                id_character = int(answers['scenchar'])  
                table = Table.load(answers['table_id'])
                if table:
                    if table.add_basicplayer(Session().player, id_character):
                        print('Successfully added to the table.')
                    else:
                        print('Something went wrong when you tried to join the table.')
                else:
                    print('Table not found.')
            
            return PlayerMenuView()



        elif Session().user_type == 'organiser':
            from view.organiser_view.menu_view import OrganiserMenuView
                        
            if answers['scenchar'][0:5] == 'Error':
                return OrganiserMenuView()
            
            from business.table.table import Table
            if answers['role'] == 'Game Master':
                id_scenario = int(answers['scenchar'])
                table = Table.load(answers['table_id'])
                if table:
                    if table.add_gamemaster(self.player, id_scenario):
                        print('Successfully added to the table.')
                        message = 'You\'ve been moved, check your tables !'
                        Session().organiser.notify_player(notif=message, username=self.player.username)

                    else:
                        print('Something went wrong when you tried to add the player to the table')
                else:
                    print('Table not found.')
                    
            if answers['role'] == 'Basic Player':
                id_character = int(answers['scenchar'])  
                table = Table.load(answers['table_id'])
                if table:
                    if table.add_basicplayer(self.player, id_character):
                        print('Successfully added to the table.')
                        message = 'You\'ve been moved, check your tables !'
                        Session().organiser.notify_player(notif=message, username=self.player.username)

                    else:
                        print('Something went wrong when you tried to add the player to the table.')
                else:
                    print('Table not found.')
            
            return OrganiserMenuView()
            