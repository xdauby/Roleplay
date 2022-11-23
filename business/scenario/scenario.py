

class Scenario:
    
    def __init__(self, name:str, description:str, id:int = None, username:str = None) -> None:
        
        self.id = id
        self.username = username
        self.name = name
        self.description = description

    def __str__(self) -> str:
        return f'Scenario \n Id : {self.id} \n Name : {self.name} \n Description : {self.description}'

    def __eq__(self, obj) -> bool:
        if isinstance(obj,Scenario):
            if self.id == obj.id and self.username == obj.username and self.name == obj.name and self.description == obj.description:
                return True
        return False