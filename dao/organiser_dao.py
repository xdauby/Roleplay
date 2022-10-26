from typing import List, Optional
from dao.db_connection import DBConnection
from business.user.organiser import Organiser
from business.notification.notification import Notification

class OrganiserDao:

    def load(self, username:str):

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
            organiser = Organiser(res['firstname'], res['lastname'], res['username'], res['age'])
        return organiser

    def save_notif(self, notif: Notification):

        request = "INSERT INTO notif(notif, username) VALUES "\
        "(%(username)s, %(notif)s)"\
        "RETURNING id_notif;"

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request 
                ,{"username" : notification.belong_to
                 ,"notif" : notification.notif })
                res = cursor.fetchone()
        if res:
            notification.id = res['id_notif']
            created = True

        return created   

