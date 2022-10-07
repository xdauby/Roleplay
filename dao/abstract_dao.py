from typing import List, Optional
from dao.db_connection import DBConnection

from abc import ABC, abstractmethod

class Dao(ABC):
    
    @abstractmethod
    def add(self) -> bool:
        pass

    @abstractmethod
    def rm(self) -> bool:
        pass

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def load_all(self) -> List:
        pass
    