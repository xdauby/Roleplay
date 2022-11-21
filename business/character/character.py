from webservice.api_dd_v2 import ApiDungeonDragon

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
        desc_race = ApiDungeonDragon().get_description(race = self.race)
        if desc_race['race']:
            return True
        return False
    def check_equipment(self) -> bool:
        desc_equipment = ApiDungeonDragon().get_description(equipment=self.equipment)
        print(desc_equipment['equipment'])
        if desc_equipment['equipment']:
            return True
        return False
    def check_skill(self) -> bool:
        desc_skill = ApiDungeonDragon().get_description(skills=self.skill)
        if desc_skill['skills']:
            return True
        return False
    
    def __str__(self) -> str:
        return f'Character \n Id : {self.id} \n Name : {self.name} \n  race : {self.race} \n  equipment : {self.equipment} \n  skill : {self.skill}'
    
    def __eq__(self, obj) -> bool:
        if isinstance(obj,Character):
            if self.id == obj.id and self.username == obj.username and self.name == obj.name and self.level == obj.level and self.race == obj.race and self.skill == obj.skill and self.equipment == obj.equipment:
                return True
        return False