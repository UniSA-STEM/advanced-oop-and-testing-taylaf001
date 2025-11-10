'''
File: reptile.py
Description: This file contains code for the Animal child class 'reptile'.
Author: Tayla Fontanabella
ID: Taylaf001
Username: Fonty005
This is my own work as defined by the University's Academic Integrity Policy.
'''
from animal import Animal

class Reptile(Animal):
    def __init__(self, name, classification, species, age, dietary_requirements, specialisation_needed, preferred_environment, preferred_space, is_venomous):
        # Animal class attributes
        super().__init__(name, classification, species, age, dietary_requirements, specialisation_needed, preferred_environment, preferred_space)

        # Empty Attributes which include data validation to ensure only valid inputs are passed in and set
        self.__is_venomous = is_venomous

        if isinstance(is_venomous, bool):
            self.__is_venomous = is_venomous
        else:
            raise TypeError("Set venomous to either True or False")

    # Getter
    def get_venomous(self):
        return self.__is_venomous

    # Setter
    def set_is_venomous(self, is_venomous):
        self.__is_venomous = is_venomous

    # Methods including abstract ones from animal class
    def making_sounds(self):
        print(f"{self.get_name()} makes a sound.. *hiss*")

    def eating(self):
        print(f"{self.get_name()} lunges for their food.. *chomp*")

    def sleeping(self):
        print(f"{self.get_name()} goes to sleep in a hidden spot... *zzzzz*")

    def shed_skin(self):
        print(f"{self.get_name()} sheds its skin, revealing a glossy new look..")

    def bask_insun(self):
        print(f"{self.get_name()} basks in the sun, absorbing vitamin D and warming up..")

    def hunt(self):
        print(f"{self.get_name()} stalks its prey, ready to strike at any moment..")