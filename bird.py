'''
File: bird.py
Description: This file contains code for the Animal child class 'bird'.
Author: Tayla Fontanabella
ID: Taylaf001
Username: Fonty005
This is my own work as defined by the University's Academic Integrity Policy.
'''
from animal import Animal

class Bird(Animal):
    def __init__(self, name, classification, species, age, dietary_requirements, specialisation_needed, preferred_environment, preferred_space, can_fly):
        # Animal class attributes
        super().__init__(name, classification, species, age, dietary_requirements, specialisation_needed, preferred_environment, preferred_space)

        # Attributes which include data validation to ensure only valid inputs are passed in and set
        self.__can_fly = can_fly

        if isinstance(can_fly, bool):
            self.__can_Fly = can_fly
        else:
            raise TypeError("Set 'Can fly' to either True or False")

    # Getter
    def get_can_fly(self):
        return self.__can_fly

    # Setter
    def set_can_fly(self, can_fly):
        self.__can_Fly = can_fly

    # Methods including abstract ones from animal class
    def making_sounds(self):
        print(f"{self.get_name()} makes a sound.. *squark squark*")

    def eating(self):
        print(f"{self.get_name()} pecks at their fruit and vegetables.. *peck peck*")

    def sleeping(self):
        print(f"{self.get_name()} sleeps perched, high up in a tree... *zzzzz*")

    def fly(self):
        if self.__can_fly() == True:
            print(f"{self.get_name()} zooms through the blue sky.. *squark*")
        else:
            print(f"{self.get_name()} is unable to fly")

    def preen_feathers(self):
        print(f"{self.get_name()} carefully preens its feathers, smoothing and cleaning them..")

    def build_nest(self):
        print(f"{self.get_name()} gathers nesting material and carefully creates a cozy nest.. *peck*")

    def lay_egg(self):
        print(f"{self.get_name()} lays an egg..")
