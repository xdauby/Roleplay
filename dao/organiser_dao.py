from typing import List, Optional
from dao.db_connection import DBConnection
from business.user.organiser import Organiser
from business.notification.notification import Notification

class OrganiserDao:
    """Organiser DAO class
    """    

    def load(self, username:str) -> Organiser:
        """load Organiser

        Args:
            username (str): username of the Organiser to load

        Returns:
            Organiser: return the loaded Organiser
        """        
        organiser = None
        request = "SELECT * FROM organiser "\
                  "WHERE username = %(username)s;"

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request
                    , {"username" : username})
                res = cursor.fetchone()
        
        if res:
            organiser = Organiser(firstname=res['firstname']
                                    , lastname=res['lastname']
                                    , username=res['username']
                                    , age=res['age']
                                    , password=res['password'])
        return organiser

    def save_notif(self, notif: Notification) -> bool:
        """save notification into database

        Args:
            notif (Notification): notification to save

        Returns:
            bool: True if the notification has been saved, else False
        """        
        request = "INSERT INTO notification(username, notif) VALUES "\
                    "(%(username)s, %(notif)s)"\
                    "RETURNING id_notif;"

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request 
                ,{"username" : notif.username
                 ,"notif" : notif.notification })
                res = cursor.fetchone()
        if res:
            notif.id = res['id_notif']
            created = True

        return created   

