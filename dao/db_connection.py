from utils_.singleton import Singleton

import os

import dotenv
import psycopg2
from psycopg2.extras import RealDictCursor
from utils_.singleton import Singleton


class DBConnection(metaclass=Singleton):
    """
    Technical class to open only one connection to the DB.
    """
    def __init__(self):
        dotenv.load_dotenv(override=True)
        # Open the connection. 
        self.__connection =psycopg2.connect(host="/var/run/postgresql", port="5432", dbname="roleplay", user="postgres", password="r", cursor_factory = RealDictCursor)

    @property
    def connection(self):
        """
        return the opened connection.

        :return: the opened connection.
        """
        return self.__connection
