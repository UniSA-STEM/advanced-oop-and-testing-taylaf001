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

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.__animals.append(animal)
        else:
            raise TypeError("Animal must be an Animal object.")

    def remove_animal(self, animal):
        if isinstance(animal, Animal):
            self.__animals.remove(animal)
        else:
            raise TypeError("Animal must be an Animal object.")

    def add_enclosure(self, enclosure):
        if isinstance(enclosure, Enclosure):
            self.__enclosures.append(enclosure)
        else:
            raise TypeError("Enclosure must be an Enclosure object.")

    def remove_enclosure(self, enclosure):
        if isinstance(enclosure, Enclosure):
            self.__enclosures.remove(enclosure)
        else:
            raise TypeError("Enclosure must be an Enclosure object.")

    def add_staff(self, staff):
        if isinstance(staff, Staff):
            self.__staff.append(staff)
        else:
            raise TypeError("Staff must be an Staff object.")

    def remove_staff(self, staff):
        if isinstance(staff, Staff):
            self.__staff.remove(staff)
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




