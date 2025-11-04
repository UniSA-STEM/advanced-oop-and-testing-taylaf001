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
        Animal.__init__(self, name, classification, species, age, dietary_requirements, specialisation_needed, preferred_environment, preferred_space)

        if isinstance(is_venomous, bool):
            self.__is_venomous = is_venomous
        else:
            raise TypeError("Set venomous to either True or False")

    def get_venomous(self):
        return self.__is_venomous

    def making_sounds(self):
        print(f"{self.get_name()} makes a sound.. *hiss*")

    def eating(self):
        print(f"{self.get_name()} lunges for their food.. *chomp*")

    def sleeping(self):
        print(f"{self.get_name()} goes to sleep in a hidden spot... *zzzzz*")

    def shed_skin(self):
        print(f"{self.get_name()} sheds its skin, revealing a glossy new look..")

    def bask_InSun(self):
        print(f"{self.get_name()} basks in the sun, absorbing vitamin D and warming up..")

    def hunt(self):
        print(f"{self.get_name()} stalks its prey, ready to strike at any moment..")