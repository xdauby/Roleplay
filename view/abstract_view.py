from abc import ABC, abstractmethod

from view.session import Session


class AbstractView(ABC):
    """Abstract View

    Args:
        ABC
    """    

    @abstractmethod
    def display_info(self):
        """display info of a view
        """        
        pass

    @abstractmethod
    def make_choice(self):
        """Allows user to make choices
        """        
        pass
