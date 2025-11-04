'''
File: mammal.py
Description: This file contains code for the Animal child class 'mammals'
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
            self.__fur_type = fur_type
        else:
            print("Fur type must be a string.")

    def get_fur_type(self):
        return self.__fur_type

    def set_fur_type(self, fur_type):
        if fur_type not in self.fur_types:
            print("Invalid fur type. Please choose one from the following list:")
            for fur_type in self.fur_types:
                print(f"{fur_type}\n")
        else:
            self.__fur_type = fur_type

    def making_sounds(self):
        print(f"{Animal.get_name(self)} makes a sound.. *grrrr*")

    def eating(self):
        print(f"{Animal.get_name(self)} scoffs down some food.. *chomp chomp*")

    def sleeping(self):
        print(f"{Animal.get_name(self)} dozes off... *Zzzzz*")

    def socialise(self):
        print(f"{Animal.get_name(self)} communicates with the other {Animal.get_species(self)}'s..*vocal noises*")

    def nurse_offspring(self):
        print(f"{Animal.get_name(self)} nurses their offspring.. *nuzzles offspring*")

    def play(self):
        print(f"{Animal.get_name(self)} plays with the other {Animal.get_species(self)}'s..*playful noises*")