'''
File: zookeeper.py
Description: This file contains code for the staff child class, 'zookeeper'
Author: Tayla Fontanabella
ID: Taylaf001
Username: Fonty005
This is my own work as defined by the University's Academic Integrity Policy.
'''
from animal import Animal
from staff import Staff
from enclosure import Enclosure

class Zookeeper(Staff):

    def __init__(self, name, staffID, role):
        # Staff class attributes
        super().__init__(name, staffID, role)

        # Attributes which include data validation to ensure only valid inputs are passed in and set
        self.__assigned_enclosures = []

    # Getters
    def get_assigned_enclosures(self):
        return self.__assigned_enclosures

    # Setters
    def set_assign_enclosure(self, enclosure):
        if isinstance(enclosure, Enclosure):
            if enclosure not in self.__assigned_enclosures: # Validation to ensure no duplication
                self.__assigned_enclosures.append(enclosure)
            else:
                print(f"Enclosure '{enclosure}' already assigned.")
        else:
            raise TypeError("Enclosure assigned to Zookeeper must be an valid enclosure object that has been added to the zoo.")

    # Methods
    def duties(self): # Abstract method from parent staff class performs all individual duties
        print(f"Zookeeper {self.get_name()} is performing assigned duties.")
        for enclosure in self.__assigned_enclosures:
            for animal in enclosure.get_animalsenclosedlist():
                print(f"Zookeeper {self.get_name()} has successfully fed {animal.get_name()}.")
            print(f"Zookeeper {self.get_name()} has thoroughly cleaned enclosure '{enclosure.get_enclosure_Name()}'.")

    def assign_enclosure(self, enclosure):
        if isinstance(enclosure, Enclosure):
            if enclosure not in self.__assigned_enclosures:
                self.set_assign_enclosure(enclosure)
            else:
                raise ValueError(f"Enclosure '{enclosure}' already assigned.")
        else:
            raise TypeError(f"No enclosure object exists with this name.")

    def unassign_enclosure(self, enclosure):
        if isinstance(enclosure, Enclosure):
            if enclosure in self.__assigned_enclosures:
                self.__assigned_enclosures.remove(enclosure)
            else:
                raise ValueError(f"Enclosure '{enclosure}' not found.")
        else:
            raise TypeError(f"No enclosure object exists with this name.")

    def feed_animal(self, animal):
        if isinstance(animal, Animal):
            for enclosure in self.__assigned_enclosures: # Access individual enclosures within assigned enclosures list
                if animal in enclosure.get_animalsenclosedlist(): # Access specific animal within the individual enclosure
                    print(f"Zookeeper {self.get_name()} has successfully fed {animal.get_name()}.")
                    return
            print(f"No animal with this name found in any enclosures.")
        else:
            raise TypeError("Animal must be an animal object already in the zoo.")

    def clean_enclosure(self, enclosure):
        if isinstance(enclosure, Enclosure):
            if enclosure in self.__assigned_enclosures:
                print(f"Zookeeper {self.get_name()} has successfully cleaned enclosure '{enclosure.get_enclosure_name()}'.")
                return
            else:
                print("No enclosure with this name has been assigned to Zookeeper.")
        else:
            raise TypeError("Enclosure must be an enclosure object already in the zoo.")

