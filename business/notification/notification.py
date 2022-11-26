
class Notification:
    """ Notification class
    """    
    def __init__(self,notification:str,username:str, id:int = None):
        """_summary_

        Args:
            notification (str): the message of the notification
            username (str): the username player who owns the Notification 
            id (int, optional):  Defaults to None.
        """        
        self.id=id
        self.notification=notification
        self.username=username
    
    def __str__(self) -> str:
        return self.notification
    
    def __eq__(self, obj) -> bool:
        if isinstance(obj,Notification):
            if self.id == obj.id and self.username == obj.username and self.notification == obj.notification:
                return True
        return False