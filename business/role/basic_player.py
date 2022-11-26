from business.character.character import Character

class BasicPlayer:
    """BasicPlayer class
        It is the player profile where characters are stored. 
    """    

    def __init__(self, username:str ) -> None:
        """init

        Args:
            username (str): the username player who owns the BasicPlayer profile
        """        

        self.username = username
        self.characters = []
        
    def add_character(self, character: Character) -> bool:
        """ add a character to the BasicPlayer profil, restricted to 3.

        Args:
            character (Character): Character to add

        Returns:
            bool: True if the Character is added to the profil, else false
        """        
        if len(self.characters) < 3:
            from dao.basic_player_dao import BasicPlayerDao
            created = BasicPlayerDao().add_character(character)
            if created:
                self.characters.append(character)
                return True
        return False


    def rm_character(self, id:int) -> bool:
        """remove Character from the profile.

        Args:
            id (int): id of the Character to delete

        Returns:
            bool:  True if the Character is removed from the profil, else false
        """        
        
        for character in self.characters:
            if character.id == id:
                from dao.basic_player_dao import BasicPlayerDao
                if BasicPlayerDao().rm_character(id):
                    self.characters.remove(character)
                    return True
        return False
    
    def __eq__(self, obj) -> bool:
        if isinstance(obj,BasicPlayer):
            if self.username == obj.username and self.characters == obj.characters:
                return True
        return False

    @staticmethod
    def load(username:str):
        """load the BasicPlayer of player identified by his username.

        Args:
            username (str): username of the player

        Returns:
            BasicPlayer : return the loaded BasicPlayer profile
        """        
        from dao.basic_player_dao import BasicPlayerDao
        return BasicPlayerDao().load(username)


