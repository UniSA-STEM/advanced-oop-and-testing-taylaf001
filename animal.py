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
    # Dictionaries utilised in class to store key-value pairs unique to each classification of animal and ensure all are applied to every animal object
    animal_preferredEnvironment = {"Mammal": ("Grassland", "Tropical", "Savanna", "Farm", "Backyard", "Indoors"),
                                    "Bird": ("Aviary", "Tropical", "Grassland", "Wetlands", "Urban"),
                                    "Reptile": ("Desert", "Tropical", "Terrarium", "Aquatic")}

    animal_preferredSpecialists = {"Mammal": "Mammal",
                                   "Bird": "Avian",
                                   "Reptile": "Exotic"}

    # List to store set values that can be used across all classifications and species
    animal_preferredSpace = ["Small", "Medium", "Large"]
    animal_preferredDiet = ["Carnivore", "Omnivore", "Herbivore"]
    animal_classifications = ["Bird", "Mammal", "Reptile"]

    def __init__(self, name, classification, species, age, dietary_requirements, specialisation_needed, preferred_environment, preferred_space):
        # Empty Attributes which include data validation to ensure only valid inputs are passed in and set
        self.__name = name
        self.__classification = classification
        self.__species = species
        self.__age = age
        self.__dietary_requirements = dietary_requirements
        self.__specialisation_needed = specialisation_needed
        self.__preferred_environment = preferred_environment
        self.__preferred_space = preferred_space
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

    # Getters

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

    # Setters

    def set_dietary_requirements(self, dietary_requirements):
        if dietary_requirements not in self.animal_preferredDiet:
            raise ValueError(f"An animal's diet must be chosen from the list: {self.animal_preferredDiet}")
        else:
            self.__dietary_requirements = dietary_requirements

    def set_classification(self, classification):
        if classification not in self.animal_classifications:
            raise ValueError(f"Classification must be chosen from the list: {self.animal_classifications}")
        else:
            self.__classification = classification

    def set_species(self, species):
        self.__species = species

    def set_specialisation_needed(self, specialisation_needed):
        required_specialist = self.animal_preferredSpecialists.get(self.__classification) # Sets the required specialist to the animals specific classification
        if specialisation_needed == required_specialist:
            self.__specialisation_needed = specialisation_needed
        else:
            raise ValueError(f"Your {self.__species} requires a {required_specialist} veterinarian.")

    def set_preferred_environment(self, preferred_environment):
        preferredEnvironment = self.animal_preferredEnvironment.get(self.__classification) # Sets the preferred environment to the animals specific environment
        if preferred_environment in preferredEnvironment:
            self.__preferred_environment = preferred_environment
        else:
            raise ValueError(f"Invalid environment for {self.__species}. Please choose from {preferredEnvironment}.")

    def set_preferred_space(self, preferred_space):
        if preferred_space in self.animal_preferredSpace:
            self.__preferred_space = preferred_space
        else:
            raise ValueError(f"Invalid space. Please choose from {self.animal_preferredSpace}.")

    # Methods
    def health_report(self):
        return f"{self.__health.generate_animalreport(self.__name, self.__classification, self.__species, self.__age)}"

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

    # String conversion
    def __str__(self):
        return f"Your animal, {self.__name}, has been successfully introduced into the Zoo.\n"
