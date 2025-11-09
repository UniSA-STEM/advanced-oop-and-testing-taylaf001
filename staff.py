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
    roles = ["Veterinarian, Zookeeper"]
    used_StaffID = set()
    def __init__(self, name, staffID, role):

        self.__name = name
        self.__staffID = staffID
        self.__role = role

        if isinstance(name, str):
            self.__name = name
        else:
            raise TypeError("Name must be a string.")

        if isinstance(role, str):
            self.set_role(role)
        else:
            raise TypeError("Role must be a string.")

        if isinstance(staffID, int):
            if staffID > 0 and staffID < 9999:
                self.set_staffID(staffID)
            else:
                raise ValueError("Staff ID must be a 4 digit number.")
        else:
            raise TypeError("Staff ID must be a number.")

    # Getters
    def get_name(self):
        return self.__name

    def get_role(self):
        return self.__role

    def get_staffID(self):
        return self.__staffID

    # Setters
    def set_role(self, role):
        if role in self.roles:
            self.__role = role
        else:
            raise ValueError(f"Staff role must be from the list: {self.roles}")

    def set_staffID(self, staffID):
        if staffID in self.used_StaffID:
            raise ValueError(f"Staff ID: {staffID} already exists. Please enter a unique 4 digit number.")
        else:
            self.used_StaffID.add(staffID)
            self.__staffID = staffID

    # Methods
    @abstractmethod
    def duties(self):
        pass
