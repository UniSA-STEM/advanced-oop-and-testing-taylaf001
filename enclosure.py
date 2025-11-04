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
    enclosure_Sizes = ["Small", "Medium", "Large"]
    enclosure_Environments = ["Grassland", "Tropical", "Savanna", "Farm", "Backyard", "Indoors", "Aviary", "Tropical", "Grassland", "Wetlands", "Urban", "Desert", "Tropical", "Terrarium", "Aquatic"]

    def __init__(self, enclosure_Name, size, environment, species_Assigned, max_Capacity, cleanliness_Level=100):
        if isinstance(enclosure_Name, str):
            self.__enclosure_Name = enclosure_Name
        else:
            raise TypeError("Enclosure name must be a string.")

        if isinstance(size, str):
            self.set_size(size)
        else:
            raise TypeError("Enclosure size must be a string.")


    def set_size(self, size):
        if size in self.enclosure_Sizes:
            self.__size = size
        else:
            raise ValueError(f"Enclosure size must be selected from the following:{self.enclosure_Sizes}")
