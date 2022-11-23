from typing import List, Optional

from dao.db_connection import DBConnection
from business.user.player import Player
from dao.basic_player_dao import BasicPlayerDao
from dao.game_master_dao import GameMasterDao
from business.notification.notification import Notification


class PlayerDao:

    def load(self, username:str) -> Player:

        player = None
        request = "SELECT * FROM player "\
                  "WHERE username = %(username)s;"

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request
                    , {"username" : username})
                res = cursor.fetchone()
        
        if res:
            notif = self.load_notif(username)
            player = Player(firstname=res['firstname']
                            , lastname=res['lastname']
                            , username=res['username']
                            , age=res['age']
                            , password=res['password']
                            , notification=notif)
            
            game_master = GameMasterDao().load(username)
            basic_player = BasicPlayerDao().load(username)
            
            player.game_master = game_master
            player.basic_player = basic_player

            halfday_tables_id = self.player_halfday_and_tables_id(username)

            player.halfday = halfday_tables_id['halfday']
            player.tables = halfday_tables_id['tables_id']

        return player


    def delete(self, username:str) -> bool:

        deleted = False

        request = 'DELETE FROM player WHERE username=%(username)s;'\
                    'DELETE FROM char_reg_game WHERE id_game in '\
                    '(SELECT game.id_game FROM player '\
                    'LEFT JOIN scenario ON player.username=scenario.username '\
                    'LEFT JOIN game on game.id_scenario = scenario.id_scenario '\
                    'WHERE player.username=%(username)s);'\
                    'SELECT * FROM player WHERE username=%(username)s;'

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                    cursor.execute(
                        request, 
                        {'username': username})
                    res = cursor.fetchall()
        
        if not res: 
            deleted = True

        return deleted

    def save(self, player:Player) -> bool:
         
        created = False
        request = "INSERT INTO player(username, firstname, lastname, age, password) VALUES "\
                  "(%(username)s,%(firstname)s,%(lastname)s,%(age)s,%(password)s)"\
                  "RETURNING username;"
        
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request
                , {"username" : player.username
                  ,"firstname" : player.firstname
                  ,"lastname" : player.lastname 
                  ,"age": player.age
                  ,'password': player.password})
                res = cursor.fetchone()
        if res:
            created = True

        return created

    def load_notif(self,username) -> Notification:
        
        notif = None
        request = "SELECT * FROM notification WHERE username  = %(username)s ORDER BY id_notif DESC LIMIT 1;"
        
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request
                , {"username" : username
                  })
                res = cursor.fetchone()
        
        if res:
            notif = Notification(notification=res['notif'], username=res['username'], id=res['id_notif'])
        
        return notif

    def delete_notif(self, username:str) -> bool:

        deleted = False
        
        request = 'DELETE FROM notification WHERE username  = %(username)s;'\
                  'SELECT * FROM notification WHERE username  = %(username)s;'     
            
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request
                , {"username" : username
                  })
                res = cursor.fetchone()
        if not res:
            deleted = True
        return deleted

    def player_halfday_and_tables_id(self,username: str):

        halfday = []
        tables_id = []

        request = 'SELECT game.halfday, game.id_game FROM game '\
                        'LEFT JOIN char_reg_game on game.id_game = char_reg_game.id_game '\
                        'INNER JOIN character on character.id_char = char_reg_game.id_char '\
                        'WHERE character.username = %(username)s '\
                        'UNION '\
                        'SELECT game.halfday, game.id_game FROM game '\
                        'LEFT JOIN scenario on scenario.id_scenario = game.id_scenario '\
                        'WHERE scenario.username = %(username)s;'            

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                    cursor.execute(
                        request, 
                        {'username': username})
                    res = cursor.fetchall()

        halfday = []
        for rows in res:
            halfday.append(rows['halfday']) 
            tables_id.append(rows['id_game'])
      
        return {'halfday' : halfday, 'tables_id': tables_id}


