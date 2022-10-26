from typing import List, Optional

from dao.db_connection import DBConnection
from business.user.abstract_player import Player
from dao.basic_player_dao import BasicPlayerDao
from dao.game_master_dao import GameMasterDao

class PlayerDao:

    def load(self, username:str):

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
            
            player = Player(res['firstname'], res['lastname'], res['username'], res['age'])
            
            game_master = GameMasterDao().load(username)
            basic_player = BasicPlayerDao().load(username)
            
            player.game_master = game_master
            player.basic_player = basic_player
            player_tables = basic_player.tables_id + game_master.tables_id
            player.halfday = self.player_halfday(username)

        return player

    def player_halfday(self,username: str):

        halfday = []

        request = 'SELECT game.halfday FROM game '\
                        'LEFT JOIN char_reg_game on game.id_game = char_reg_game.id_game '\
                        'INNER JOIN character on character.id_char = char_reg_game.id_char '\
                        'WHERE character.username = %(username)s '\
                        'UNION '\
                        'SELECT game.halfday FROM game '\
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
      
        return halfday

    def save(self, player:Player):
         
        created = False
        request = "INSERT INTO player(username, firstname, lastname, age) VALUES "\
                  "(%(username)s,%(firstname)s,%(lastname)s, %(age)s)"\
                  "RETURNING username;"
        
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request
                , {"username" : player.username
                  ,"firstname" : player.firstname
                  ,"lastname" : player.lastname 
                  ,"age": player.age})
                res = cursor.fetchone()
        if res:
            created = True

        return created

    def load_notif(self,username):
        request = "SELECT TOP 1 notif FROM notif WHERE player.username  = %(username)s ORDER BY DESC id";

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request
                , {"username" : player.username
                  ,"firstname" : player.firstname
                  ,"lastname" : player.lastname 
                  ,"age": player.age})
                res = cursor.fetchone()
        if res:
            return res







