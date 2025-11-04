'''
File: mammal.py
Description: This file contains code for the Animal child class 'mammal'
Author: Tayla Fontanabella
ID: Taylaf001
Username: Fonty005
This is my own work as defined by the University's Academic Integrity Policy.
'''
from animal import Animal

class Mammal(Animal):
    fur_types = ["None", "Soft", "Coarse", "Long", "Short"]
    def __init__(self, name, classification, species, age, dietary_requirements, specialisation_needed, preferred_environment, preferred_space, fur_type):
        Animal.__init__(self, name, classification, species, age, dietary_requirements, specialisation_needed, preferred_environment, preferred_space)

        if isinstance(fur_type, str):
            self.set_fur_type(fur_type)
        else:
            raise TypeError("Fur type must be a string.")

    def get_fur_type(self):
        return self.__fur_type

    def set_fur_type(self, fur_type):
        if fur_type not in self.fur_types:
            raise ValueError(f"Invalid fur type. Please choose from {self.fur_types}.")
        else:
            self.__fur_type = fur_type
            print(f"{self.get_name()}'s fur type is {self.__fur_type}.")

    def making_sounds(self):
        print(f"{self.get_name()} makes a sound.. *grrrr*")

    def eating(self):
        print(f"{self.get_name()} scoffs down some food.. *chomp chomp*")

    def sleeping(self):
        print(f"{self.get_name()} dozes off... *zzzzz*")

    def socialise(self):
        print(f"{self.get_name()} communicates with the other {self.get_species()}s.. *vocal noises*")

    def nurse_offspring(self):
        print(f"{self.get_name()} nurses their offspring.. *nuzzles offspring*")

    def play(self):
        print(f"{self.get_name()} plays with the other {self.get_species()}s.. *playful noises*")