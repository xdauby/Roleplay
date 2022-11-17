import requests as req

class ApiDungeonDragon:
    
    def __init__(self) -> None:

        self.root:str = 'https://www.dnd5eapi.co'
        self.equipment_path: str = '/api/equipment'
        self.race_path: str = '/api/races'
        self.skills_path: str = '/api/skills'

    def get_features_list(self) -> dict:

        list_equipment_fetch = req.get(self.root + self.equipment_path).json()['results']
        list_race_fetch = req.get(self.root + self.race_path).json()['results']
        list_skills_fetch = req.get(self.root + self.skills_path).json()['results']

        list_equipments = []
        list_races = []
        list_skills = []

        for i in range(len(list_equipment_fetch)):
            list_equipments.append(list_equipment_fetch[i]['name'])

        for i in range(len(list_race_fetch)):
            list_races.append(list_race_fetch[i]['name'])

        for i in range(len(list_skills_fetch)):
            list_skills.append(list_skills_fetch[i]['name'])

        features = {
            'equipments' : list_equipments,
            'skills' : list_skills,
            'races' : list_races
        }

        return features

    def get_description(self, equipment: str = None, race: str = None, skills: str = None):

        if equipment is None and race is None and skills is None :
            return "Specify what you want a descrition of"
        
        if equipment is not None:
            equipment_desc = req.get(self.root + self.equipment_path + '/' + equipment).json()['desc']
            return equipment_desc
        
        elif race is not None:
            race_fetch = req.get(self.root + self.race_path + '/' + race).json()

            race_speed = race_fetch['speed']
            race_languages = race_fetch['language_desc']
            race_age = race_fetch['age']
            race_size = race_fetch['size']

            race_desc = f'Race speed is {race_speed}, size is {race_size}. {race_age} {race_languages}'
            return race_desc

        elif skills is not None:
            skills_desc = req.get(self.root + self.skills_path + '/' + skills).json()['desc']
            return skills_desc
