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
    enclosure_sizes = ["Small", "Medium", "Large"]
    enclosure_environments = ["Grassland", "Tropical", "Savanna", "Farm", "Backyard", "Indoors", "Aviary", "Tropical", "Grassland", "Wetlands", "Urban", "Desert", "Tropical", "Terrarium", "Aquatic"]

    def __init__(self, enclosure_name, size, environment, animal_assigned, max_capacity):

        self.__enclosure_name = enclosure_name
        self.__size = size
        self.__environment = environment
        self.__animal_assigned = animal_assigned
        self.__max_capacity = max_capacity
        self.__cleanliness_level = 100
        self.__current_capacity = 0
        self.__animalsencloseddict = {}

        if isinstance(enclosure_name, str):
            self.__enclosure_name = enclosure_name
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

        if isinstance(animal_assigned, str):
            self.set_animal_assigned(animal_assigned)
        else:
            raise TypeError("Animal assigned must be a string.")

        if isinstance(max_capacity, int):
            self.__max_Capacity = max_capacity
        else:
            raise TypeError("Max capacity must be a number.")

        print(self)

    # Getters
    def get_enclosure_name(self):
        return self.__enclosure_name

    def get_size(self):
        return self.__size

    def get_environment(self):
        return self.__environment

    def get_animal_assigned(self):
        return self.__animal_assigned

    def get_max_capacity(self):
        return self.__max_capacity

    def get_current_capacity(self):
        return self.__current_capacity

    def get_cleanliness_level(self):
        return self.__cleanliness_level

    def get_animalsenclosedlist(self):
        return self.__animalsencloseddict

    # Setters
    def set_cleanliness_level(self, cleanliness_level):
        self.__cleanliness_level = cleanliness_level

    def set_size(self, size):
        if size in self.enclosure_sizes:
            self.__size = size
        else:
            raise ValueError(f"Enclosure size must be selected from the following:{self.enclosure_sizes}")

    def set_environment(self, environment):
        if environment in self.enclosure_environments:
            self.__environment = environment
        else:
            raise ValueError(f"Enclosure environment must be selected from the following:{self.enclosure_environments}")

    def set_animal_assigned(self, animal_assigned):
        if animal_assigned in Animal.animal_classifications:
            self.__animal_assigned = animal_assigned
        else:
            raise ValueError(f"Animal classification assigned must be selected from {Animal.animal_classifications}")

    def set_animalsenclosed(self, animal):
        self.__animalsencloseddict.update({animal.get_name(): animal}) # Add animal to enclosed animals dictionary

    def set_current_capacity(self, current_capacity):
        if isinstance(current_capacity, int):
            self.__current_capacity = current_capacity
        else:
            raise TypeError("Current capacity must be a number.")

    # Methods
    def add_animal(self, animal): # Adds animal into enclosure IF their health status is not sick or under treatment
        if isinstance(animal, Animal):
            if animal.get_name() not in self.__animalsencloseddict:
                if animal.get_health().get_health_status() == "Sick":
                    raise ValueError(f"{animal.get_name()} cannot be moved to the enclosure due to it's health status.")
                elif animal.get_health().get_health_status() == "Under Treatment":
                    raise ValueError(f"{animal.get_name()} cannot be moved to the enclosure due to it's health status.")
                # if statements used as data validation to ensure animals are assigned into enclosures that suit their needs
                if animal.get_classification() == self.__animal_assigned and self.__current_capacity < self.__max_capacity and animal.get_preferred_environment() == self.__environment and animal.get_preferred_space() == self.__size:
                    self.set_animalsenclosed(animal)
                    self.set_current_capacity(self.get_current_capacity()+1)
                    print(f"{animal.get_name()} has been successfully introduced into the {self.__enclosure_name}.\n")
                elif animal.get_classification() == self.__animal_assigned and self.__current_capacity == self.__max_capacity and animal.get_preferred_environment() == self.__environment and animal.get_preferred_space() == self.__size:
                    raise ValueError(f"Enclosure capacity full. Remove an animal or build a new enclosure.")
                elif animal.get_classification() == self.__animal_assigned and self.__current_capacity < self.__max_capacity and animal.get_preferred_environment() != self.__environment and animal.get_preferred_space() == self.__size:
                    raise ValueError(f"Enclosure environment not {animal.get_name()}'s preferred environment.")
                elif animal.get_classification() == self.__animal_assigned and self.__current_capacity < self.__max_capacity and animal.get_preferred_environment() == self.__environment and animal.get_preferred_space() != self.__size:
                    raise ValueError(f"Enclosure size not {animal.get_name()}'s preferred enclosure size.")
                elif animal.get_classification() == self.__animal_assigned and self.__current_capacity < self.__max_capacity and animal.get_preferred_environment() != self.__environment and animal.get_preferred_space() != self.__size:
                    raise ValueError(f"Enclosure size and environment do not meet {animal.get_name()}'s preferred specifications.")
                else:
                    raise ValueError(f"Animal must match species assigned to enclosure: {self.__animal_assigned}")
            else:
                raise ValueError(f"{animal.get_name()} already in the enclosure. Animal cannot be added twice.")
        else:
            raise TypeError(f"No animal object exists with this name.")

    def remove_animal(self, animal): # Searches key value pairs for animal name, if found, ensure animal health status not under treatment or sick, then remove key value pair.
        if isinstance(animal, Animal):
            if animal.get_health().get_health_status() != "Under Treatment" and animal.get_health().get_health_status() != "Sick":
                if animal.get_name() in self.__animalsencloseddict:
                    self.__animalsencloseddict.pop(animal.get_name())
                    self.set_current_capacity(self.get_current_capacity()-1)
                else:
                    raise ValueError(f"{animal.get_name()} cannot be removed as it's not in the enclosure.")
            else:
                raise ValueError(f"{animal.get_name()} cannot be removed/moved due to its health status.")
        else:
            raise TypeError(f"No animal object exists with this name.")

    def list_animals(self): # Display all animals within the enclosure
        print(f"\033[1mAnimals Enclosed:\033[0m\n")
        for key, value in self.__animalsencloseddict.items(): # Display each animal and their details in the stored dictionary
            print(f"\033[1mName:\033[0m {key} | \033[1mSpecies:\033[0m {value.get_species()} | \033[1mAge:\033[0m {value.get_age()} | \033[1mClassification:\033[0m {value.get_classification()}")

    def enclosure_status(self):
        print("------------------------")
        print(f"\033[1m{self.__enclosure_name} Report:\033[0m")
        print("------------------------")
        print(f"\033[1mEnclosure Environment:\033[0m {self.__environment}")
        print(f"\033[1mSpecies Assigned:\033[0m {self.__animal_assigned}")
        print(f"\033[1mCleanliness Level:\033[0m {self.__cleanliness_level}")
        print(f"\033[1mCurrent Capacity:\033[0m {self.__current_capacity}")
        print(f"\033[1mMax Capacity:\033[0m {self.__max_capacity}")
        print("----")
        self.list_animals()
        print("----------------------")
        # Code inspired by:
        # Kodeclik, 2025. How to bold text in python. [Online] Kodeclik.
        # Available at: <https://www.kodeclik.com/how-to-bold-text-in-python/>
        # [Accessed 6 November 2025].

    # String conversion method
    def __str__(self):
        return f"{self.__enclosure_name} has successfully been added to the zoo.\n"
