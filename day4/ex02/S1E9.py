from abc import ABC, abstractmethod


class Character(ABC):
    """" the parent"""

    def __init__(self, first_name, is_alive = True):
        """init function"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """the abstract function"""
        pass
    #your code here


class Stark(Character):
    """the abstract class"""
    #your code here
    def die(self):
        """ the die function from the abstract class"""
        self.is_alive = False
    