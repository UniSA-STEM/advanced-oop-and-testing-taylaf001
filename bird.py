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
    def __init__(self, name, classification, species, age, dietary_requirements, specialisation_needed, preferred_environment, preferred_space, can_Fly):
        # Animal class attributes
        Animal.__init__(self, name, classification, species, age, dietary_requirements, specialisation_needed, preferred_environment, preferred_space)

        # Empty Attributes which include data validation to ensure only valid inputs are passed in and set
        self.__can_Fly = None

        if isinstance(can_Fly, bool):
            self.__can_Fly = can_Fly
        else:
            raise TypeError("Set 'Can fly' to either True or False")

    # Getter
    def get_can_Fly(self):
        return self.__can_Fly

    # Setter
    def set_can_Fly(self, can_Fly):
        self.__can_Fly = can_Fly

    # Methods including abstract ones from animal class
    def making_sounds(self):
        print(f"{self.get_name()} makes a sound.. *squark squark*")

    def eating(self):
        print(f"{self.get_name()} pecks at their fruit and vegetables.. *peck peck*")

    def sleeping(self):
        print(f"{self.get_name()} sleeps perched, high up in a tree... *zzzzz*")

    def fly(self):
        if self.get_can_Fly() == True:
            print(f"{self.get_name()} zooms through the blue sky.. *squark*")
        else:
            print(f"{self.get_name()} is unable to fly")

    def preen_feathers(self):
        print(f"{self.get_name()} carefully preens its feathers, smoothing and cleaning them..")

    def build_Nest(self):
        print(f"{self.get_name()} gathers nesting material and carefully creates a cozy nest.. *peck*")

    def lay_Egg(self):
        print(f"{self.get_name()} lays an egg..")
