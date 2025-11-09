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
    specialisations = ["Mammal", "Avian", "Exotic"]

    def __init__(self, name, staffID, role, specialisation):
        super().__init__(name, staffID, role)

        self.__specialisation = specialisation
        self.__assigned_Animals = []

        if isinstance(specialisation, str):
            self.set_specialisation(specialisation)
        else:
            raise TypeError(f"Specialisation must be a string.")

    # Getters
    def get_specialisation(self):
        return self.__specialisation

    def get_assigned_Animals(self):
        return self.__assigned_Animals

    # Setters
    def set_specialisation(self, specialisation):
        if specialisation in self.specialisations:
            self.__specialisation = specialisation
        else:
            raise ValueError(f"Veterinary specialisation must be selected from the list: {self.specialisations}")

    def set_assign_Animal(self, animal):
        if isinstance(animal, Animal): # Validation that the animal passed through is a match for the Animal object.
            if animal.get_specialisation_needed() == self.get_specialisation():
                self.__assigned_Animals.append(animal)
            else:
                print(f"Veterinarian selected does not have the correct specialisation for your animal. Please select a {animal.get_specialisation_needed()} veterinarian.")
        else:
            raise TypeError(f"Animal assigned to veterinarian must be an animal object already in the zoo.")
    # Methods
    def assign_Animal(self, animal):
        self.set_assign_Animal(animal)

    def duties(self): # Perform health check on all assigned animals
        print(f"Dr {self.get_name()} is performing assigned duties.")
        for animal in self.get_assigned_Animals():
            print(f"Dr {self.get_name()} has successfully performed a health check on {animal.get_name()}.")

    def perform_HealthCheck(self, animal): # Perform health check on specific animal
        if isinstance(animal, Animal):
            if animal in self.get_assigned_Animals():
                print(f"Dr {self.get_name()} is conducting a health check on {animal.get_name()}.")
            else:
                raise ValueError(f"Animal not in assigned list. Please select an animal from the list: {self.get_assigned_Animals()}")
        else:
            raise TypeError(f"Animal assigned to veterinarian must be an animal object already in the zoo.")


