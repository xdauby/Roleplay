

class Notification:
    def __init__(self,notification:str,username:str, id:int = None):
        
        self.id=id
        self.notification=notification
        self.username=username
    
    def __str__(self):
        return self.notification