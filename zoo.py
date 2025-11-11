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
            if animal not in self.__animals:
                self.__animals.append(animal)
                print(f"{animal.get_name()} has been introduced into the zoo.\n")
            else:
                raise ValueError("Animal already exists in the zoo.")
        else:
            raise TypeError("Animal must be an Animal object.")

    def remove_animal(self, animal):
        if isinstance(animal, Animal):
            if animal in self.__animals:
                self.__animals.remove(animal)
                print(f"{animal.get_name()} has been removed from the zoo.\n")
            else:
                raise ValueError("Animal not in the zoo.")
        else:
            raise TypeError("Animal must be an Animal object.")

    def add_enclosure(self, enclosure):
        if isinstance(enclosure, Enclosure):
            if enclosure not in self.__enclosures:
                self.__enclosures.append(enclosure)
                print(f"Enclosure: {enclosure.get_enclosure_name()} has been built in the zoo.\n")
            else:
                raise ValueError("Enclosure already exists in the zoo.")
        else:
            raise TypeError("Enclosure must be an Enclosure object.")

    def remove_enclosure(self, enclosure):
        if isinstance(enclosure, Enclosure):
            if enclosure in self.__enclosures:
                self.__enclosures.remove(enclosure)
                print(f"{enclosure.get_enclosure_name()} has been demolished and land has been flattened.\n")
            else:
                raise ValueError("Enclosure does not exist in the zoo.")
        else:
            raise TypeError("Enclosure must be an Enclosure object.")

    def add_staff(self, staff):
        if isinstance(staff, Staff):
            if staff not in self.__staff:
                self.__staff.append(staff)
                print(f"{staff.get_role()} {staff.get_name()} has been hired and inducted into the zoo.\n")
            else:
                raise ValueError("Staff already exists in the zoo.")
        else:
            raise TypeError("Staff must be an Staff object.")

    def remove_staff(self, staff):
        if isinstance(staff, Staff):
            if staff in self.__staff:
                self.__staff.remove(staff)
                print(f"{staff.get_name()} has been removed from the zoo.\n")
            else:
                raise ValueError("Staff does not exist in the zoo.")
        else:
            raise TypeError("Staff must be an Staff object.")

    def show_staff(self):
        for staff in self.__staff:
            print(f"| \033[1mName:\033[0m {staff.get_name()} | \033[1mRole:\033[0m {staff.get_role()} | \033[1mStaff ID:\033[0m {staff.get_staffID()} |")

    def show_enclosures(self):
        for enclosure in self.__enclosures:
            print(f"| \033[1mName:\033[0m {enclosure.get_enclosure_name()} | \033[1mAnimal Assigned:\033[0m {enclosure.get_animal_assigned()} | \033[1mEnvironment:\033[0m {enclosure.get_environment()} | \033[1mCurrent Capacity:\033[0m {enclosure.get_current_capacity()} | \033[1mCleanliness Level:\033[0m {enclosure.get_cleanliness_level()} |")

    def show_animals(self):
        for animal in self.__animals:
            print(f"| \033[1mName:\033[0m {animal.get_name()} | \033[1mClassification:\033[0m {animal.get_classification()} | \033[1mSpecies:\033[0m {animal.get_species()} | \033[1mAge:\033[0m {animal.get_age()} | \033[1mHealth Status:\033[0m {animal.get_health().get_health_status()} |")

    def daily_routine(self):
        print("=========================")
        print("== Daily Routine ==")
        for staff in self.__staff:
            staff.duties()
        print("=========================")

    def list_animals(self):
        print("=========================")
        print("== Animals in Zoo ==")
        for animal in self.__animals:
            print(f"| Name: {animal.get_name()} | Classification: {animal.get_classification()} | Species: {animal.get_species()} | Age: {animal.get_age()} | Health Status: {animal.get_health().get_health_status()} |\n")
        print("=========================")

    def enclosure_statuses(self):
        print("=========================")
        print("== Enclosures Statuses ==")
        for enclosure in self.__enclosures:
            enclosure.enclosure_status()
        print("=========================")

    def zoo_report(self):
        print("=========================")
        print(f"== \033[1m{self.get_name()} Overview\033[0m ==")
        print("=========================")
        print("\n\033[1mStaff:\033[0m")
        self.show_staff()
        print("\n\033[1mEnclosures:\033[0m")
        self.show_enclosures()
        print("\n\033[1mAnimals:\033[0m")
        self.show_animals()
        print("=========================")
        # Code inspired by:
        # Kodeclik, 2025. How to bold text in python. [Online] Kodeclik.
        # Available at: <https://www.kodeclik.com/how-to-bold-text-in-python/>
        # [Accessed 6 November 2025].



