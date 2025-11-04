'''
File: enclosure.py
Description: Enclosure.py contains code related to Animal enclosures.
Author: Tayla Fontanabella
ID: taylaf001
Username: Fonty005
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Enclosure:
    enclosure_Sizes = ["Small", "Medium", "Large"]
    enclosure_Environments = ["Grassland", "Tropical", "Savanna", "Farm", "Backyard", "Indoors", "Aviary", "Tropical", "Grassland", "Wetlands", "Urban", "Desert", "Tropical", "Terrarium", "Aquatic"]

    def __init__(self, enclosure_Name, size, environment, animal_Assigned, max_Capacity):
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

        self.__cleanliness_Level = 100

        self.__animalsEnclosedDict = {}

        self.__current_Capacity = 0

        print(self)

    def get_max_Capacity(self):
        return self.__max_Capacity

    def get_current_Capacity(self):
        return self.__current_Capacity

    def get_cleanliness_Level(self):
        return self.__cleanliness_Level

    def get_animalsEnclosedList(self):
        return self.__animalsEnclosedDict

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

    def add_animal(self, animal):
        if animal.get_classification() == self.__animal_Assigned and self.__current_Capacity < self.__max_Capacity and animal.get_preferred_environment() == self.__environment and animal.get_preferred_space() == self.__size:
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
        print(f"Animals Enclosed:\n")
        for key, value in self.__animalsEnclosedDict.items():
            print(f"Name: {key} | Species: {value.get_species()} | Age: {value.get_age()} | Classification: {value.get_classification()}")

    def enclosure_status(self):
        print("------------------------")
        print(f"{self.__enclosure_Name} Status:")
        print("-----")
        print(f"Enclosure Environment: {self.__environment}")
        print(f"Species Assigned: {self.__animal_Assigned}")
        print(f"Cleanliness Level: {self.__cleanliness_Level}")
        print(f"Current Capacity: {self.__current_Capacity}")
        print(f"Max Capacity: {self.__max_Capacity}")
        print("-----")
        self.list_animals()
        print("----------------------")

    def __str__(self):
        return f"{self.__enclosure_Name} has successfully been added to the zoo.\n"
