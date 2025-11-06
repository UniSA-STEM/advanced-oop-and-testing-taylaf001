'''
File: staff.py
Description: Staff.py contains code for the parent class 'staff'.
Author: Tayla Fontanabella
ID: Taylaf001
Username: Fonty005
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod

class Staff(ABC):
    def __init__(self, name, role):

        self.__name = name
        self.__role = role

        if isinstance(name, str):
            self.__name = name
        else:
            raise TypeError("Name must be a string.")

        if isinstance(role, str):
            self.__role = role
        else:
            raise TypeError("Role must be a string.")

    def assigned_animals(self):

    def assigned_enclosures(self):
