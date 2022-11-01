

class Notification:
    def __init__(self,notification:str,username:str, id:int = None):
        
        self.id=id
        self.notification=notification
        self.username=username
    
    def __str__(self):
        return self.notification
    
    def __eq__(self, obj):
        if isinstance(obj,Notification):
            if self.id == obj.id and self.username == obj.username and self.notification == obj.notification:
                return True
        return False