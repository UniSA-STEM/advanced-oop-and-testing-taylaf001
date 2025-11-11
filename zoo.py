'''
File: zoo.py
Description: zoo.py file acts as the central zoo management file to prevent clutter in main.py testing file.
Author: Tayla Fontanabella
ID: taylaf001
Username: Fonty005
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal
from enclosure import Enclosure
from staff import Staff


class Zoo:
    def __init__(self, name):
        self.__name = name
        self.__enclosures = []
        self.__animals = []
        self.__staff = []

        if isinstance(name, str):
            self.set_name(name)
        else:
            raise TypeError("Name must be a string.")

    # Getters
    def get_name(self):
        return self.__name

    def get_enclosures(self):
        return self.__enclosures

    def get_animals(self):
        return self.__animals

    def get_staff(self):
        return self.__staff

    # Setters
    def set_name(self, name):
        self.__name = name

    # Methods
    def add_animal(self, animal):
        if isinstance(animal, Animal):
            if animal not in self.get_animals():
                self.__animals.append(animal)
                print(f"{animal.get_name()} has been introduced into the zoo.")
            else:
                raise ValueError("Animal already exists in the zoo.")
        else:
            raise TypeError("Animal must be an Animal object.")

    def remove_animal(self, animal):
        if isinstance(animal, Animal):
            if animal in self.get_animals():
                self.__animals.remove(animal)
                print(f"{animal.get_name()} has been removed from the zoo.")
            else:
                raise ValueError("Animal not in the zoo.")
        else:
            raise TypeError("Animal must be an Animal object.")

    def add_enclosure(self, enclosure):
        if isinstance(enclosure, Enclosure):
            if enclosure not in self.get_enclosures():
                self.__enclosures.append(enclosure)
                print(f"{enclosure.get_enclosure_name()} has been built into the zoo.")
            else:
                raise ValueError("Enclosure already exists in the zoo.")
        else:
            raise TypeError("Enclosure must be an Enclosure object.")

    def remove_enclosure(self, enclosure):
        if isinstance(enclosure, Enclosure):
            if enclosure in self.get_enclosures():
                self.__enclosures.remove(enclosure)
                print(f"{enclosure.get_enclosure_name()} has been demolished and land has been flattened.")
            else:
                raise ValueError("Enclosure does not exist in the zoo.")
        else:
            raise TypeError("Enclosure must be an Enclosure object.")

    def add_staff(self, staff):
        if isinstance(staff, Staff):
            if staff not in self.get_staff():
                self.__staff.append(staff)
                print(f"{staff.get_name()} has been hired and inducted into the zoo.")
            else:
                raise ValueError("Staff already exists in the zoo.")
        else:
            raise TypeError("Staff must be an Staff object.")

    def remove_staff(self, staff):
        if isinstance(staff, Staff):
            if staff in self.get_staff():
                self.__staff.remove(staff)
                print(f"{staff.get_name()} has been removed from the zoo.")
            else:
                raise ValueError("Staff does not exist in the zoo.")
        else:
            raise TypeError("Staff must be an Staff object.")

    def daily_routine(self):
        print("== Daily Routine ==")
        for staff in self.__staff:
            staff.duties()
        print("===================")

    def list_animals(self):
        print("== Animals in Zoo ==")
        for animal in self.__animals:
            print(f"| Name:{animal.get_name()} | Classification:{animal.get_classification()} - Species:{animal.get_species()} | Age:{animal.get_age()} | Health Status:{animal.health.get_health_status()} |\n")
        print("====================")

    def enclosure_statuses(self):
        print("== Enclosures Statuses==")
        for enclosure in self.__enclosures:
            print(f"{enclosure.enclosure_status()}\n")
        print("====================")




