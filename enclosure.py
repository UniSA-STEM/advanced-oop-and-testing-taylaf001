'''
File: enclosure.py
Description: Enclosure.py contains code related to Animal enclosures.
Author: Tayla Fontanabella
ID: taylaf001
Username: Fonty005
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal
from health import Health

class Enclosure:
    enclosure_Sizes = ["Small", "Medium", "Large"]
    enclosure_Environments = ["Grassland", "Tropical", "Savanna", "Farm", "Backyard", "Indoors", "Aviary", "Tropical", "Grassland", "Wetlands", "Urban", "Desert", "Tropical", "Terrarium", "Aquatic"]

    def __init__(self, enclosure_Name, size, environment, animal_Assigned, max_Capacity):

        self.__enclosure_Name = enclosure_Name
        self.__size = size
        self.__environment = environment
        self.__animal_Assigned = animal_Assigned
        self.__max_Capacity = max_Capacity
        self.__cleanliness_Level = 100
        self.__current_Capacity = 0
        self.__animalsEnclosedDict = {}

        if isinstance(enclosure_Name, str):
            self.__enclosure_Name = enclosure_Name
        else:
            raise TypeError("Enclosure name must be a string.")

        if isinstance(size, str):
            self.set_size(size)
        else:
            raise TypeError("Enclosure size must be a string.")

        if isinstance(environment, str):
            self.set_environment(environment)
        else:
            raise TypeError("Enclosure environment must be a string.")

        if isinstance(animal_Assigned, str):
            self.set_animal_Assigned(animal_Assigned)
        else:
            raise TypeError("Animal assigned must be a string.")

        if isinstance(max_Capacity, int):
            self.__max_Capacity = max_Capacity
        else:
            raise TypeError("Max capacity must be a number.")

        print(self)

    # Getters
    def get_enclosure_Name(self):
        return self.__enclosure_Name

    def get_size(self):
        return self.__size

    def get_environment(self):
        return self.__environment

    def get_animal_Assigned(self):
        return self.__animal_Assigned

    def get_max_Capacity(self):
        return self.__max_Capacity

    def get_current_Capacity(self):
        return self.__current_Capacity

    def get_cleanliness_Level(self):
        return self.__cleanliness_Level

    def get_animalsEnclosedList(self):
        return self.__animalsEnclosedDict

    # Setters
    def set_cleanliness_Level(self, cleanliness_Level):
        self.__cleanliness_Level = cleanliness_Level

    def set_size(self, size):
        if size in self.enclosure_Sizes:
            self.__size = size
        else:
            raise ValueError(f"Enclosure size must be selected from the following:{self.enclosure_Sizes}")

    def set_environment(self, environment):
        if environment in self.enclosure_Environments:
            self.__environment = environment
        else:
            raise ValueError(f"Enclosure environment must be selected from the following:{self.enclosure_Environments}")

    def set_animal_Assigned(self, animal_Assigned):
        if animal_Assigned in Animal.animal_Classifications:
            self.__animal_Assigned = animal_Assigned
        else:
            raise ValueError(f"Animal classification assigned must be selected from {Animal.animal_Classifications}")

    def set_animalsEnclosed(self, animal):
        self.__animalsEnclosedDict.update({animal.get_name(): animal})

    def set_current_Capacity(self, current_Capacity):
        self.__current_Capacity = current_Capacity

    # Methods
    def add_animal(self, animal):
        if animal.health.get_health_Status() == "Sick":
            return print(f"{animal.get_name()} cannot be moved to the enclosure due to it's health status.")
        elif animal.health.get_health_Status() == "Under Treatment":
            return print(f"{animal.get_name()} cannot be moved to the enclosure due to it's health status.")

        if animal.get_classification() == self.__animal_Assigned and self.__current_Capacity < self.__max_Capacity and animal.get_preferred_environment() == self.__environment and animal.get_preferred_space() == self.__size and animal.health.get_health_Status() != "Sick" and animal.health.get_health_Status() != "Under Treatment":
            self.set_animalsEnclosed(animal)
            self.set_current_Capacity(self.get_current_Capacity()+1)
            print(f"{animal.get_name()} has been successfully introduced into the {self.__enclosure_Name}.\n")
        elif animal.get_classification() == self.__animal_Assigned and self.__current_Capacity == self.__max_Capacity and animal.get_preferred_environment() == self.__environment and animal.get_preferred_space() == self.__size:
            raise ValueError(f"Enclosure capacity full. Remove an animal or build a new enclosure.")
        elif animal.get_classification() == self.__animal_Assigned and self.__current_Capacity < self.__max_Capacity and animal.get_preferred_environment() != self.__environment and animal.get_preferred_space() == self.__size:
            raise ValueError(f"Enclosure environment not {animal.get_name()}'s preferred environment.")
        elif animal.get_classification() == self.__animal_Assigned and self.__current_Capacity < self.__max_Capacity and animal.get_preferred_environment() == self.__environment and animal.get_preferred_space() != self.__size:
            raise ValueError(f"Enclosure size not {animal.get_name()}'s preferred enclosure size.")
        elif animal.get_classification() == self.__animal_Assigned and self.__current_Capacity < self.__max_Capacity and animal.get_preferred_environment() != self.__environment and animal.get_preferred_space() != self.__size:
            raise ValueError(f"Enclosure size and environment do not meet {animal.get_name()}'s preferred specifications.")
        else:
            raise ValueError(f"Animal must match species assigned to enclosure: {self.__animal_Assigned}")

    def remove_animal(self, animal):
        for animal in self.__animalsEnclosedDict.keys():
            if animal.get_name() == animal:
                self.__animalsEnclosedDict.pop(animal)
                self.set_current_Capacity(self.get_current_Capacity()-1)

    def list_animals(self):
        print(f"\033[1mAnimals Enclosed:\033[0m\n")
        for key, value in self.__animalsEnclosedDict.items():
            print(f"\033[1mName:\033[0m {key} | \033[1mSpecies:\033[0m {value.get_species()} | \033[1mAge:\033[0m {value.get_age()} | \033[1mClassification:\033[0m {value.get_classification()}")

    def enclosure_status(self):
        print("------------------------")
        print(f"\033[1m{self.__enclosure_Name} Report:\033[0m")
        print("------------------------")
        print(f"\033[1mEnclosure Environment:\033[0m {self.__environment}")
        print(f"\033[1mSpecies Assigned:\033[0m {self.__animal_Assigned}")
        print(f"\033[1mCleanliness Level:\033[0m {self.__cleanliness_Level}")
        print(f"\033[1mCurrent Capacity:\033[0m {self.__current_Capacity}")
        print(f"\033[1mMax Capacity:\033[0m {self.__max_Capacity}")
        print("----")
        self.list_animals()
        print("----------------------")

    # String conversion method
    def __str__(self):
        return f"{self.__enclosure_Name} has successfully been added to the zoo.\n"
