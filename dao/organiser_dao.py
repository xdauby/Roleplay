from typing import List, Optional
from dao.db_connection import DBConnection
from business.user.organiser import Organiser

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

