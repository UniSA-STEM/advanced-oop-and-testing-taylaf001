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

    # Dictionaries utilised to store key-value pairs unique to each classification of animal
    animal_PreferredEnvironments = {"Mammal": ("Grassland", "Tropical", "Savanna", "Farm", "Backyard", "Indoors"),
                                    "Bird": ("Aviary", "Tropical", "Grassland", "Wetlands", "Urban"),
                                    "Reptile": ("Desert", "Tropical", "Terrarium", "Aquatic")}
    animal_PreferredSpecialists = {"Mammal": "Mammal", "Bird": "Avian", "Reptile": "Exotic"}

    # List to store set values that can be used across all classifications and species
    animal_PreferredSpace = ["Small", "Medium", "Large"]
    animal_PreferredDiet = ["Carnivore", "Omnivore", "Herbivore"]
    animal_Classifications = ["Bird", "Mammal", "Reptile"]

    def __init__(self, name, classification, species, age, dietary_requirements, specialisation_needed, preferred_environment, preferred_space):
        # Attributes which include data validation to ensure only valid inputs are passed in
        if isinstance(name, str):
            self.__name = name
        else:
            print("Name must be a string")

        if isinstance(classification, str):
            self.__classification = classification
        else:
            print("Classification must be a string")

        if isinstance(species, str):
            self.__species = species
        else:
            print("Species must be a string")

        if isinstance(age, int):
            self.__age = age
        else:
            print("Age must be a number")

        if isinstance(dietary_requirements, str):
            self.__dietary_requirements = dietary_requirements
        else:
            print("Dietary requirements must be a string")

        if isinstance(specialisation_needed, str):
            self.__specialisation_needed = specialisation_needed
        else:
            print("Specialisation needed must be a string")

        if isinstance(preferred_environment, str):
            self.__preferred_environment = preferred_environment
        else:
            print("Preferred environment must be a string")

        if isinstance(preferred_space, str):
            self.__preferred_space = preferred_space
        else:
            print("Preferred space must be a string")

        self.__health = Health() #NEED TO DO HEALTH CLASS BEFORE DOING THIS

    # Getters for attributes
    def get_name(self):
        return self.__name

    def get_species(self):
        return self.__species

    def get_age(self):
        return self.__age

    def get_dietary_requirements(self):
        return self.__dietary_requirements

    def get_specialisation_needed(self):
        return self.__specialisation_needed

    def get_preferred_environment(self):
        return self.__preferred_environment

    def get_preferred_space(self):
        return self.__preferred_space

    def get_classification(self):
        return self.__classification

    # Setters for attributes
    def set_dietary_requirements(self, dietary_requirements):
        if dietary_requirements not in animal_PreferredDiet:
            print("An animal must either be a Carnivore, Herbivore, or Omnivore")
        else:
            self.__dietary_requirements = dietary_requirements

    def set_classification(self, classification):
        if classification not in animal_Classifications:
            print("Classification must be either Mammal, Bird or Reptile")
        else:
            self.__classification = classification

    def set_species(self, species):
        self.__species = species

    def set_specialisation_needed(self, specialisation_needed):
        required_specialist = animal_PreferredSpecialists.get(self.__classification)
        if specialisation_needed == required_specialist:
            print(f"Your animal [{self.__classification}] has been assigned to a {self.__specialisation_needed} veterinarian.")
        else:
            print(f"Your animal [{self.__classification}] requires a {required_specialist} veterinarian.")

    def set_preferred_environment(self, preferred_environment):
        preferredEnvironment = animal_PreferredEnvironment.get(self.__classification)
        if preferred_environment in preferredEnvironment:
            self.__preferred_environment = preferred_environment
            print(f"Your animal [{self.__classification}]'s preferred environment is {preferredEnvironment}.")
        else:
            print(f"Your animal [{self.__classification}]'s environment can be set to one of the following:")
            for value in preferredEnvironment:
                print(f"{value}")

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

