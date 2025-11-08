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
    animal_PreferredEnvironment = {"Mammal": ("Grassland", "Tropical", "Savanna", "Farm", "Backyard", "Indoors"),
                                    "Bird": ("Aviary", "Tropical", "Grassland", "Wetlands", "Urban"),
                                    "Reptile": ("Desert", "Tropical", "Terrarium", "Aquatic")}
    animal_PreferredSpecialists = {"Mammal": "Mammal", "Bird": "Avian", "Reptile": "Exotic"}

    # List to store set values that can be used across all classifications and species
    animal_PreferredSpace = ["Small", "Medium", "Large"]
    animal_PreferredDiet = ["Carnivore", "Omnivore", "Herbivore"]
    animal_Classifications = ["Bird", "Mammal", "Reptile"]

    def __init__(self, name, classification, species, age, dietary_requirements, specialisation_needed, preferred_environment, preferred_space):
        # Empty Attributes which include data validation to ensure only valid inputs are passed in and set
        self.__name = None
        self.__classification = None
        self.__species = None
        self.__age = None
        self.__dietary_requirements = None
        self.__specialisation_needed = None
        self.__preferred_environment = None
        self.__preferred_space = None
        self.__health = Health()

        if isinstance(name, str):
            self.__name = name
        else:
            raise TypeError("Name must be a string.")

        if isinstance(classification, str):
            self.set_classification(classification)
        else:
            raise TypeError("Classification must be a string")

        if isinstance(species, str):
            self.set_species(species)
        else:
            raise TypeError("Species must be a string")

        if isinstance(age, int):
            self.__age = age
        else:
            raise TypeError("Age must be a number")

        if isinstance(dietary_requirements, str):
            self.set_dietary_requirements(dietary_requirements)
        else:
            raise TypeError("Dietary requirements must be a string")

        if isinstance(specialisation_needed, str):
            self.set_specialisation_needed(specialisation_needed)
        else:
            raise TypeError("Specialisation needed must be a string")

        if isinstance(preferred_environment, str):
            self.set_preferred_environment(preferred_environment)
        else:
            raise TypeError("Preferred environment must be a string")

        if isinstance(preferred_space, str):
            self.set_preferred_space(preferred_space)
        else:
            raise TypeError("Preferred space must be a string")

        print(self)

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

    def get_health(self):
        return self.__health

    # Setters for attributes

    def set_dietary_requirements(self, dietary_requirements):
        if dietary_requirements not in self.animal_PreferredDiet:
            raise ValueError("An animal must either be a Carnivore, Herbivore, or Omnivore")
        else:
            self.__dietary_requirements = dietary_requirements

    def set_classification(self, classification):
        if classification not in self.animal_Classifications:
            raise ValueError("Classification must be either Mammal, Bird or Reptile")
        else:
            self.__classification = classification

    def set_species(self, species):
        self.__species = species

    def set_specialisation_needed(self, specialisation_needed):
        required_specialist = self.animal_PreferredSpecialists.get(self.__classification)
        if specialisation_needed == required_specialist:
            self.__specialisation_needed = specialisation_needed
        else:
            raise ValueError(f"Your {self.__species} requires a {required_specialist} veterinarian.")

    def set_preferred_environment(self, preferred_environment):
        preferredEnvironment = self.animal_PreferredEnvironment.get(self.__classification)
        for environment in preferredEnvironment:
            if environment == preferred_environment:
                self.__preferred_environment = preferred_environment
        if preferred_environment not in preferredEnvironment:
            raise ValueError(f"Invalid environment for {self.__species}. Please choose from {preferredEnvironment}.")


    def set_preferred_space(self, preferred_space):
        if preferred_space in self.animal_PreferredSpace:
            self.__preferred_space = preferred_space
        else:
            raise ValueError(f"Invalid space. Please choose from {self.animal_PreferredSpace}.")

    # Methods
    def health_report(self):
        return f"{self.__health.generate_AnimalReport(self.__name, self.__classification, self.__species, self.__age)}"

    # String conversion
    def __str__(self):
        return f"Your animal, {self.get_name()}, has been successfully introduced into the Zoo.\n"

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

