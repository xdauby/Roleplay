from typing import List, Optional
from dao.db_connection import DBConnection
from dao.abstract_dao import Dao
from business.scenario.scenario import Scenario


class ScenarioDao(Dao):

    
    def add(self, scenario:Scenario) -> bool:

        created = False
        request = "INSERT INTO scenario(username, name, description) VALUES "\
                  "(%(username)s,%(name)s,%(description)s)"\
                  "RETURNING id_scenario;"
        
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request
                , {"username" : scenario.belong_to
                  ,"name" : scenario.name
                  ,"description" : scenario.description })
                res = cursor.fetchone()
        if res:
            scenario.id = res['id_scenario']
            created = True

        return created

    def rm(self) -> bool:
        pass

    def load(self, id:int):

        scenario = None
        request = "SELECT * FROM scenario WHERE id_scenario=%(id)s"
        
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request
                , {"id" : id})
                res = cursor.fetchone()

        if res:
            scenario = Scenario(name=res['name'], description=res['description'], id = res['id_scenario'])
        return scenario

    def load_user_scenarios(self, username:str):

        scenarios = None
        request = "SELECT * FROM scenario WHERE username=%(username)s"
        
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request
                , {"username" : username})
                res = cursor.fetchall()

        if res:
            scenarios = []
            for row in res:
                curr_scenario = Scenario(name=row['name'], description=row['description'], id = row['id_scenario'])
                scenarios.append(curr_scenario)
        return scenarios

    def load_all(self):
        pass
