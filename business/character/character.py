
class Character:
    
    def __init__(self, name:str, level:int, race:str, equipment: str, skill:str, id:int = None, username:str = None) -> None:
        
        self.id = id
        self.username = username

        self.name = name
        self.level = level
        
        self.race = race
        self.equipment = equipment
        self.skill = skill
        
    
    def check_race(self) -> bool:
        pass
    def check_equipment(self) -> bool:
        pass
    def check_skill(self) -> bool:
        pass
    
    def __str__(self) -> str:
        return f'Character \n Id : {self.id} \n Name : {self.name} \n  race : {self.race} \n  equipment : {self.equipment} \n  skill : {self.skill}'
    
    def __eq__(self, obj) -> bool:
        if isinstance(obj,Character):
            if self.id == obj.id and self.username == obj.username and self.name == obj.name and self.level == obj.level and self.race == obj.race and self.skill == obj.skill and self.equipment == obj.equipment:
                return True
        return False