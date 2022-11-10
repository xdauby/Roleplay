import requests as req

class ApiDungeonDragon:
    
    def __init__(self) -> None:

        self.root:str = 'https://www.dnd5eapi.co'
        self.equipment_path: str = '/api/equipment'
        self.race_path: str = '/api/races'
        self.skills_path: str = '/api/skills'

    def get_features_list(self):

        list_equipment_fetch = req.get(self.root + self.equipment_path).json()['results']
        list_race_fetch = req.get(self.root + self.race_path).json()['results']
        list_skills_fetch = req.get(self.root + self.skills_path).json()['results']

        list_equipments = []
        list_races = []
        list_skills = []

        for equipment in list_equipment_fetch[1:10]:
            
            equipment_desc = self.get_descriptions(equipment=equipment['index'])

            if equipment_desc == []:
                equipment_desc = ["No description"]
            
            temp_equipment = {
                'name': equipment['name'],
                'desc': equipment_desc[0]
            }
            list_equipments.append(temp_equipment)
    

        for race in list_race_fetch[1:10]:
            
            race_desc = self.get_descriptions(race=race['index'])
            temp_race = {
                'name': race['name'],
                'desc':race_desc
            }
            list_races.append(temp_race)
        
        for skill in list_skills_fetch[1:10]:

            
            
            skill_desc = self.get_descriptions(skills = skill['index'])

            if skill_desc == []:
                skill_desc = ["No description"]

            temp_skill = {
                'name': skill['name'],
                'desc':skill_desc[0]
            }
            list_skills.append(temp_skill)
    
        features = {
            'equipments' : list_equipments,
            'skills' : list_skills,
            'races' : list_races
        }

        return features




    def get_descriptions(self, equipment: str = None, race: str = None, skills: str = None):

        if equipment is not None:
            equipment_desc = req.get(self.root + self.equipment_path + '/' + equipment).json()['desc']
            return equipment_desc
        if race is not None:
            
            race_fetch = req.get(self.root + self.race_path + '/' + race).json()

            race_speed = race_fetch['speed']
            race_languages = race_fetch['language_desc']
            race_age = race_fetch['age']
            race_size = race_fetch['size']

            general_desc = f'Race speed is {race_speed}, size is {race_size}. {race_age} {race_languages}'
            
            return general_desc

        if skills is not None:
            skills_desc = req.get(self.root + self.skills_path + '/' + skills).json()['desc']
            return skills_desc



x = ApiDungeonDragon()
print(x.get_features_list())
