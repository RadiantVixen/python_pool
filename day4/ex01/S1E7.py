from S1E9 import Character
from abc import ABC, abstractmethod

class Baratheon(Character):
    """ Representing the Baratheon family """
    def __init__(self, first_name, is_alive =  True, family_name = 'Baratheon', eyes = 'brown', hairs = 'dark'):
        """ baratheon init"""
        Character().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')>"
    
    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')>"
    
    def die(self):
        """ die from baratheon"""
        self.is_alive = False

class Lannister(Character):
    """ Representing the lannister family """
    def __init__(self, first_name, is_alive =  True, family_name = 'Lannister', eyes = 'blue', hairs = 'light'):
        """ baratheon init"""
        Character().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def die(self):
        """die from lannister"""
        self.is_alive = False

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
    
    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """create method"""
        # Character().__init__(first_name, is_alive)
        return cls(first_name, is_alive)
    
