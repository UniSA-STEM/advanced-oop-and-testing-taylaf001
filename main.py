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
from enclosure import Enclosure
from health import Health


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

#ENCLOSURE TEST
def enclosure():
    enclosure1 = Enclosure(
        enclosure_Name="Reptile Enclosure",
        size="Small",
        environment="Desert",
        animal_Assigned="Reptile",
        max_Capacity=5
    )

    john = Reptile(
        name="John",
        classification="Reptile",
        species="Snake",
        age=27,
        dietary_requirements="Carnivore",
        specialisation_needed="Exotic",
        preferred_environment="Desert",
        preferred_space="Small",
        is_venomous=True
    )

    beep = Reptile(
        name="Beep",
        classification="Reptile",
        species="Lizard",
        age=32,
        dietary_requirements="Carnivore",
        specialisation_needed="Exotic",
        preferred_environment="Desert",
        preferred_space="Small",
        is_venomous=False
    )

    #meep = Mammal(
        #name="Meep",
        #classification="Mammal", # Testing classifications
        #species="Crocodile",
        #age=89,
        #dietary_requirements="Carnivore",
        #specialisation_needed = "Mammal",
        #preferred_environment = "Savanna", # Testing environments
        #preferred_space = "Large", # Testing space variations
        #fur_type = "Coarse"
    #)

    #matilda = Bird(
        #name="Matilda",
        #classification="Bird",
        #species="Lorikeet",
        #age=18,
        #dietary_requirements="Omnivore",
        #specialisation_needed="Avian",
        #preferred_environment="Urban",
        #preferred_space="Medium",
        #can_Fly=True
    #)

    # Add compatible animals to enclosure

    enclosure1.add_animal(john)
    enclosure1.add_animal(beep)

    # Testing adding animals that are not the enclosures assigned species

    #enclosure1.add_animal(meep)
    #enclosure1.add_animal(matilda)

    enclosure1.enclosure_status()

# Health Test
def test_Health():

    leo = Mammal(
        name="Leo",
        classification="Mammal",
        species="Elephant",
        age=18,
        dietary_requirements="Herbivore",
        specialisation_needed="Mammal",
        preferred_environment="Savanna",
        preferred_space="Large",
        fur_type="Coarse"
    )
    leo.making_sounds()
    leo.eating()
    leo.sleeping()
    leo.socialise()
    leo.nurse_offspring()
    leo.play()

    leo.health = Health()
    leo.health.update_HealthIssue("4/11/2021", "Illness", "Infection", "Infection in eye", "Minor", "XXX medication provided", "Under Treatment")
    leo.health.update_HealthIssue("2/03/2020", "Illness", "Parasites", "Parasites in stomach", "Minor", "XXX medication provided", "Under Treatment")
    leo.health.update_HealthIssue("01/11/2015", "Injury", "Broken Bone", "Broken left tibia", "Critical", "Surgery scheduled", "Under Treatment")
    leo.health.update_HealthIssue("18/08/2025", "Injury", "Broken Bone", "Broken toe", "Minor", "Bandaged", "Healthy")
    leo.health.update_HealthIssue("23/06/2024", "Injury", "Broken Bone", "Broken right tibia", "Minor", "Surgery scheduled", "Under Treatment")
    leo.health.update_HealthIssue("19/11/2019", "Illness", "Parasites", "Parasites in intestines", "Major", "XXX medication provided", "Sick")
    leo.health.generate_AnimalReport(leo.get_name(), leo.get_classification(), leo.get_species(), leo.get_age())

    enclosure1 = Enclosure(
        enclosure_Name="Mammal Enclosure",
        size="Large",
        environment="Savanna",
        animal_Assigned="Mammal",
        max_Capacity=5
    )
    enclosure1.enclosure_status()
    enclosure1.add_animal(leo)

healthTest = test_Health()


