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
            list_equipments.append(list_equipment_fetch[i]['index'])

        for i in range(len(list_race_fetch)):
            list_races.append(list_race_fetch[i]['index'])

        for i in range(len(list_skills_fetch)):
            list_skills.append(list_skills_fetch[i]['index'])

        features = {
            'equipments' : list_equipments,
            'skills' : list_skills,
            'races' : list_races
        }

        return features

    def get_description(self, equipment: str = None, race: str = None, skills: str = None):

        description = {
            'equipment' : None,
            'race' : None,
            'skills': None 
        }
        
        if equipment is not None:
            try:
                equipment_desc = req.get(self.root + self.equipment_path + '/' + equipment).json()['desc']
                if equipment_desc[0]:
                    description['equipment'] = equipment_desc[0]
                else:
                    description['equipment'] = 'No description available'
            except:
                pass

        if race is not None:
            try:
                race_fetch = req.get(self.root + self.race_path + '/' + race).json()

                race_speed = race_fetch['speed']
                race_languages = race_fetch['language_desc']
                race_age = race_fetch['age']
                race_size = race_fetch['size']

                race_desc = f'Race speed is {race_speed}, size is {race_size}. {race_age} {race_languages}'
                description['race'] = race_desc
            except:
                pass

        if skills is not None:
            try:
                skills_desc = req.get(self.root + self.skills_path + '/' + skills).json()['desc']

                if skills_desc[0]:
                    description['skills'] = skills_desc[0]
                else:
                    description['skills'] = 'No description available'
            except:
                pass
        
        return description
