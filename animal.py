'''
File: Animal.py
Description: Animal.py module contains the code for parent class 'Animal'.
Author: Tayla Fontanabella
ID: Taylaf001
Username: fonty005
This is my own work as defined by the University's Academic Integrity Policy.
'''
from abc import ABC, abstractmethod
from health import Health

class Animal(ABC):
    def __init__(self, name, species, age, dietary_requirements, specialisation_needed, preferred_environment, preferred_space, assigned_enclosure=None):
        # Attributes which include data validation to ensure only valid inputs are passed in
        if isinstance(name, str):
            self.name = name
        else:
            print("Name must be a string")

        if isinstance(species, str):
            self.species = species
        else:
            print("Species must be a string")

        if isinstance(age, int):
            self.age = age
        else:
            print("Age must be a number")

        if isinstance(dietary_requirements, str):
            self.dietary_requirements = dietary_requirements
        else:
            print("Dietary requirements must be a string")

        if isinstance(specialisation_needed, str):
            self.specialisation_needed = specialisation_needed
        else:
            print("Specialisation needed must be a string")

        if isinstance(preferred_environment, str):
            self.preferred_environment = preferred_environment
        else:
            print("Preferred environment must be a string")

        if isinstance(preferred_space, str):
            self.preferred_space = preferred_space
        else:
            print("Preferred space must be a string")

        self.health = Health()

        if isinstance(assigned_enclosure, str):
            self.assigned_enclosure = assigned_enclosure
        else:
            print("Assigned enclosure must be a string")


    # Getters for attributes
    def get_name(self):
        return self.name

    def get_species(self):
        return self.species

    def get_age(self):
        return self.age

    def get_dietary_requirements(self):
        return self.dietary_requirements

    def get_specialisation_needed(self):
        return self.specialisation_needed

    def get_preferred_environment(self):
        return self.preferred_environment

    def get_preferred_space(self):
        return self.preferred_space

    def get_assigned_enclosure(self):
        return self.assigned_enclosure

    # Common animal methods to be utilised by child classes. Abstract methods utilised to allow for customisation via child classes.
    @abstractmethod
    def making_sounds(self):
        pass

    @abstractmethod
    def eating(self):
        pass

    @abstractmethod
    def sleeping(self):
        pass

