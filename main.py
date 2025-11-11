'''
File: main.py
Description: main.py file is used for demonstration purposes.
Author: Tayla Fontanabella
ID: taylaf001
Username: Fonty005
This is my own work as defined by the University's Academic Integrity Policy.
'''

from mammal import Mammal
from bird import Bird
from reptile import Reptile
from enclosure import Enclosure
from veterinarian import Veterinarian
from zookeeper import Zookeeper
from zoo import Zoo


def tarongaZoo():
    # Generate Zoo
    tarongaZoo = Zoo("Taronga Zoo")
    print("====================================")
    print(f"Welcome to {tarongaZoo.get_name()}!")
    print("====================================")

    # Generate and Add Animals to Zoo
    ellie = Mammal("Ellie", "Mammal", "Elephant", 14, "Herbivore", "Mammal", "Savanna", "Large", "None")
    ed = Reptile("Ed", "Reptile", "Snake", 4, "Carnivore", "Exotic", "Desert", "Medium",True)
    mike = Bird("Mike", "Bird", "Macaw", 39, "Omnivore", "Avian", "Tropical", "Large", True)

    tarongaZoo.add_animal(ellie)
    tarongaZoo.add_animal(ed)
    tarongaZoo.add_animal(mike)
    print("-------------------------------------")

    # Generate and Add Staff to Zoo
    lily = Veterinarian("Lily", 4872, "Veterinarian", "Avian")
    emily = Veterinarian("Emily", 5723, "Veterinarian", "Mammal")
    matthew = Veterinarian("Matthew", 3578, "Veterinarian", "Exotic")
    andrew = Zookeeper("Andrew", 1637, "Zookeeper")
    luke = Zookeeper("Luke", 9245, "Zookeeper")
    glen = Zookeeper("Glen", 6724, "Zookeeper")

    tarongaZoo.add_staff(lily)
    tarongaZoo.add_staff(emily)
    tarongaZoo.add_staff(matthew)
    tarongaZoo.add_staff(andrew)
    tarongaZoo.add_staff(luke)
    tarongaZoo.add_staff(glen)
    print("-------------------------------------")

    # Generate and Add Enclosures to Zoo
    reptileEnclosure = Enclosure("Small Reptiles", "Medium", "Desert", "Reptile", 5)
    mammalEnclosure = Enclosure("Large Mammals", "Large", "Savanna", "Mammal", 10)
    avianEnclosure = Enclosure("Parrots", "Large", "Tropical", "Bird", 8)

    tarongaZoo.add_enclosure(reptileEnclosure)
    tarongaZoo.add_enclosure(mammalEnclosure)
    tarongaZoo.add_enclosure(avianEnclosure)
    print("-------------------------------------")

    # Assign animals to enclosures and call animal methods
    reptileEnclosure.add_animal(ed)
    ed.shed_skin()
    ed.hunt()
    ed.sleeping()
    ed.bask_insun()
    ed.eating()
    ed.making_sounds()
    print("-------------------------------------")

    mammalEnclosure.add_animal(ellie)
    ellie.eating()
    ellie.sleeping()
    ellie.making_sounds()
    ellie.nurse_offspring()
    ellie.play()
    ellie.socialise()
    print("-------------------------------------")

    avianEnclosure.add_animal(mike)
    mike.eating()
    mike.sleeping()
    mike.making_sounds()
    mike.preen_feathers()
    mike.fly()
    mike.build_nest()
    mike.lay_egg()
    print(f"{mike.get_can_fly()}") # Data retrieval example
    print("-------------------------------------")

    # Assign staff animals + enclosures to conduct daily duties
    lily.assign_animal(mike)
    emily.assign_animal(ellie)
    matthew.assign_animal(ed)
    print("-------------------------------------")

    andrew.assign_enclosure(reptileEnclosure)
    luke.assign_enclosure(mammalEnclosure)
    glen.assign_enclosure(avianEnclosure)

    # Method Demonstrations

    # Conduct Daily Duties
    tarongaZoo.daily_routine()

    # Animal Health System Usage

    # Add Health Issues & Generate Reports to display functionality
    mike.get_health().update_healthissue("05/11/2025", "Injury", "Sprain", "Sprained wing", "Minor", "No treatment necessary", "Healthy")
    mike.get_health().update_healthissue("11/11/2025", "Illness", "Infection", "Minor toe infection", "Minor", "Mike given 0.5ml dose of antibiotics", "Under Treatment")
    mike.health_report()

    ellie.health_report()

    ed.get_health().update_healthissue("04/10/2025", "Behavioural Concern", "Territorial", "Territorial of shelter", "Minor", "Observation - no treatment necessary", "Healthy")
    ed.health_report()

    # Display health history example
    print("-------------------------------------")
    print("Mike's Health History:")
    print(f"{mike.get_health().get_health_history()}")
    print("-------------------------------------")


    # List all animals in the zoo
    tarongaZoo.list_animals()

    # List animals in enclosures
    reptileEnclosure.list_animals()
    print("-------------------------------------")
    avianEnclosure.list_animals()
    print("-------------------------------------")
    mammalEnclosure.list_animals()

    # Display statuses of all enclosures in the zoo
    tarongaZoo.enclosure_statuses()

    # Display staff in zoo
    print("Staff:")
    tarongaZoo.show_staff()

    # Display Animals in zoo
    print("Animals:")
    tarongaZoo.show_animals()

    # Display enclosures in zoo
    print("Enclosures:")
    tarongaZoo.show_enclosures()

    # Display overview of all animals, staff and enclosures in zoo
    tarongaZoo.zoo_report()

    # Remove animal from enclosure then remove from zoo
    reptileEnclosure.remove_animal(ed)
    print("-------------------------------------")
    reptileEnclosure.list_animals()
    print("-------------------------------------")
    tarongaZoo.show_animals()
    print("-------------------------------------")
    tarongaZoo.remove_animal(ed)
    print("-------------------------------------")
    tarongaZoo.show_animals()
    print("-------------------------------------")

    # Unassign animal from vet
    lily.unassign_animal(mike)
    print(f"Lily's assigned animals: {lily.get_assigned_animals()}")
    print("-------------------------------------")

    # Unassign enclosure from zookeeper
    andrew.unassign_enclosure(reptileEnclosure)
    andrew.get_assigned_enclosures()
    print(f"Andrews assigned enclosures: {andrew.get_assigned_enclosures()}")
    print("-------------------------------------")

    # Remove staff from zoo
    tarongaZoo.remove_animal(mike)
    tarongaZoo.show_staff()

tarongaZoo()





