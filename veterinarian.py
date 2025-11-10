'''
File: veterinarian.py
Description: This file contains code for the staff child class, 'veterinarians'.
Author: Tayla Fontanabella
ID: Taylaf001
Username: Fonty005
This is my own work as defined by the University's Academic Integrity Policy.
'''

from staff import Staff
from animal import Animal

class Veterinarian(Staff):
    # List to store set values unique to veterinarians for access and comparison in methods
    specialisations = ["Mammal", "Avian", "Exotic"]

    def __init__(self, name, staffID, role, specialisation):
        # Staff class attributes
        super().__init__(name, staffID, role)

        # Attributes which include data validation to ensure only valid inputs are passed in and set
        self.__specialisation = specialisation
        self.__assigned_animals = []

        if isinstance(specialisation, str):
            self.set_specialisation(specialisation)
        else:
            raise TypeError(f"Specialisation must be a string.")

    # Getters
    def get_specialisation(self):
        return self.__specialisation

    def get_assigned_animals(self):
        return self.__assigned_animals

    # Setters
    def set_specialisation(self, specialisation):
        if specialisation in self.specialisations:
            self.__specialisation = specialisation
        else:
            raise ValueError(f"Veterinary specialisation must be selected from the list: {self.specialisations}")

    def set_assign_animal(self, animal):
        if isinstance(animal, Animal): # Validation that the animal passed through is a valid Animal object.
            if animal.get_specialisation_needed() == self.get_specialisation():
                self.__assigned_animals.append(animal)
            else:
                print(f"Veterinarian selected does not have the correct specialisation for your animal. Please select a {animal.get_specialisation_needed()} veterinarian.")
        else:
            raise TypeError(f"Animal assigned to veterinarian must be an animal object already in the zoo.")
    # Methods
    def assign_animal(self, animal):
        if isinstance(animal, Animal):
            self.set_assign_animal(animal)
        else:
            raise TypeError("Animal object not found with name provided.")

    def duties(self): # Abstract method from parent staff class performs all individual duties
        print(f"Dr {self.get_name()} is performing assigned duties.")
        for animal in self.get_assigned_animals():
            print(f"Dr {self.get_name()} has successfully performed a health check on {animal.get_name()}.")

    def perform_healthcheck(self, animal): # Perform health check on specific animal
        if isinstance(animal, Animal): # Validation that the animal passed through is a valid Animal object.
            if animal in self.get_assigned_animals():
                print(f"Dr {self.get_name()} is conducting a health check on {animal.get_name()}.")
            else:
                raise ValueError(f"Animal not in assigned list. Please select an animal from the list: {self.get_assigned_animals()}")
        else:
            raise TypeError("Animal assigned to veterinarian must be an animal object already in the zoo.")



