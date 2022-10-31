
class Character:
    
    def __init__(self, name:str, level:int, race:str, equipment: str, skill:str, id:int = None, username:str = None) -> None:
        
        self.id = id
        self.username = username

        self.name = name
        self.level = level
        
        self.race = race
        self.equipment = equipment
        self.skill = skill
        
        self.skill_desc = None
        self.equipment_desc = None
        self.race_desc = None

    
    def get_descriptions(self) -> None:
        pass
    
    def __str__(self):
        return f'Character \n Id : {self.id} \n Name : {self.name} \n  race : {self.race} \n  equipment : {self.equipment} \n  skill : {self.skill}'
    
    def __eq__(self, obj):
        if isinstance(obj,Character):
            if self.id == obj.id and self.username == obj.username and self.name == obj.name and self.level == obj.level and self.race == obj.race and self.skill == obj.skill and self.equipment == obj.equipment:
                return True
        return False