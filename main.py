'''
File: main.py
Description: main.py file is used for testing purposes.
Author: Tayla Fontanabella
ID: taylaf001
Username: Fonty005
This is my own work as defined by the University's Academic Integrity Policy.
'''
from mammal import Mammal
from bird import Bird
from reptile import Reptile


# BASIC ANIMAL CLASS TESTS
# Mammal test
def mammal():
    leo = Mammal(
        name = "Leo",
        classification = "Mammal",
        species = "Elephant",
        age = 18,
        dietary_requirements = "Herbivore",
        specialisation_needed = "Mammal",
        preferred_environment = "Savanna",
        preferred_space = "Large",
        fur_type = "Coarse"
    )
    leo.making_sounds()
    leo.eating()
    leo.sleeping()
    leo.socialise()
    leo.nurse_offspring()
    leo.play()

# Bird test
def bird():
    matilda = Bird(
        name = "Matilda",
        classification = "Bird",
        species = "Lorikeet",
        age = 18,
        dietary_requirements = "Omnivore",
        specialisation_needed = "Avian",
        preferred_environment = "Urban",
        preferred_space = "Medium",
        can_Fly= True
    )

    matilda.making_sounds()
    matilda.eating()
    matilda.sleeping()
    matilda.fly()
    matilda.build_Nest()
    matilda.lay_Egg()
    matilda.preen_feathers()

# Reptile test
def reptile():
    john = Reptile(
        name = "John",
        classification = "Reptile",
        species = "Snake",
        age = 27,
        dietary_requirements = "Carnivore",
        specialisation_needed = "Exotic",
        preferred_environment = "Desert",
        preferred_space = "Small",
        is_venomous=True
    )

    john.making_sounds()
    john.eating()
    john.sleeping()
    john.shed_skin()
    john.bask_InSun()
    john.hunt()


reptile = reptile()