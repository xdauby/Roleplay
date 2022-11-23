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

    def get_description(self, equipment: list[str] = None, race: list[str] = None, skills: list[str] = None):

        if equipment is None and race is None and skills is None :
            return "Specify what you want a description of"
        

        if equipment is not None:
            equipment_desc = []
            for eq in equipment :
                try:
                    equipment_fetch = req.get(self.root + self.equipment_path + '/' + eq).json()['desc']
                        
                    if equipment_desc:
                        equipment_desc.append(eq + ': ' + equipment_fetch[0])
                    else:
                        equipment_desc.append(eq + ': ' + 'No description available')
                except:
                    pass
        
        
        if race is not None:
            race_desc = []
            for r in race :
                try:
                    race_fetch = req.get(self.root + self.race_path + '/' + r).json()

                    if race_fetch:
                        race_speed = race_fetch['speed']
                        race_languages = race_fetch['language_desc']
                        race_age = race_fetch['age']
                        race_size = race_fetch['size']

                        race_desc.append(r + ': ' + [f'Race speed is {race_speed}, size is {race_size}. {race_age} {race_languages}'])
                    else:
                        race_desc.append(r + ': ' + 'No description available')
                except:
                    pass
            

        if skills is not None:
            skills_desc = []
            for sk in skills :
                try :
                    skills_fetch = req.get(self.root + self.skills_path + '/' + sk).json()['desc']
                    
                    if skills_fetch:
                        skills_desc.append(sk + ': ' + skills_fetch[0])
                    else :
                        skills_desc.append(sk + ': ' + 'No description avalaible')
                except :
                    pass
            
        desc = equipment_desc + race_desc + skills_desc
        return desc
