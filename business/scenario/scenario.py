

class Scenario:
    
    def __init__(self, name:str, description:str, id:int = None, username:str = None) -> None:
        
        self.id = id
        self.belong_to = username
        self.name = name
        self.description = description

    def __str__(self):
        return f'Scenario \n Id : {self.id} \n Name : {self.name} \n Description : {self.description}'