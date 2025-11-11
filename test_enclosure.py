'''
File: test_enclosure.py
Description: This file contains all tests for enclosure.py
Author: Tayla Fontanabella
ID: taylaf001
Username: Fonty005
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from enclosure import Enclosure
from mammal import Mammal
from reptile import Reptile


class TestEnclosure:
    @pytest.fixture
    def reptile1(self):
        return Reptile("Ed", "Reptile", "Crocodile", 4, "Carnivore", "Exotic", "Aquatic", "Large",False)

    @pytest.fixture
    def mammal1(self):
        return Mammal("Ellie", "Mammal", "Elephant", 14, "Herbivore", "Mammal", "Savanna", "Large", "None")

    @pytest.fixture
    def reptileEnclosure(self):
        return Enclosure("Big Reptiles", "Large", "Aquatic", "Reptile", 5)

    def test_reptileEnclosure(self, reptileEnclosure):  # Testing all attributes have been assigned correctly
        assert isinstance(reptileEnclosure, Enclosure)
        assert reptileEnclosure.get_enclosure_name() == "Big Reptiles"
        assert reptileEnclosure.get_size() == "Large"
        assert reptileEnclosure.get_environment() == "Aquatic"
        assert reptileEnclosure.get_animal_assigned() == "Reptile"
        assert reptileEnclosure.get_max_capacity() == 5

    def test_raises(self):
        with pytest.raises(TypeError): # NAME - Incorrect Type
            Enclosure(345, "Large", "Aquatic", "Reptile", 5)

        with pytest.raises(TypeError): # SIZE - Incorrect Type
            Enclosure("Big Reptiles", 345, "Aquatic", "Reptile", 5)

        with pytest.raises(ValueError): # SIZE - Incorrect Value
            Enclosure("Big Reptiles", "Kinda Small", "Aquatic", "Reptile", 5)

        with pytest.raises(TypeError): # ENVIRONMENT - Incorrect Type
            Enclosure("Big Reptiles", "Large", 234, "Reptile", 5)

        with pytest.raises(ValueError):  # ENVIRONMENT - Incorrect Value
            Enclosure("Big Reptiles", "Large", "Ocean", "Reptile", 5)

        with pytest.raises(TypeError):  # ANIMAL ASSIGNED - Incorrect Type
            Enclosure("Big Reptiles", "Large", "Aquatic", 345, 5)

        with pytest.raises(ValueError):  # ANIMAL ASSIGNED - Incorrect Value
            Enclosure("Big Reptiles", "Large", "Aquatic", "Idksdf", 5)

        with pytest.raises(TypeError):  # MAX CAPACITY - Incorrect Type
            Enclosure("Big Reptiles", "Large", "Aquatic", "Reptile", "5")

    def test_validateEnvironment(self, reptileEnclosure):
        reptileEnclosure.set_environment("Savanna")
        assert reptileEnclosure.get_environment() == "Savanna"

    def test_addAnimal(self, reptileEnclosure, reptile1): # Test adding animal to enclosure and that CAPACITY updates correctly
        reptileEnclosure.add_animal(reptile1)
        assert reptile1.get_name() in reptileEnclosure.get_animalsenclosedlist()
        assert reptileEnclosure.get_current_capacity() == 1

    def test_addSickAnimal(self, reptileEnclosure, reptile1): # Test adding SICK animal to enclosure
        reptile1.get_health().set_health_status("Sick")
        with pytest.raises(ValueError):
            reptileEnclosure.add_animal(reptile1)
        assert reptile1.get_name() not in reptileEnclosure.get_animalsenclosedlist()
        assert reptileEnclosure.get_current_capacity() == 0

    def test_addUnderTreatmentAnimal(self, reptileEnclosure, reptile1): # Test adding UNDER TREATMENT animal to enclosure
        reptile1.get_health().set_health_status("Under Treatment")
        with pytest.raises(ValueError):
            reptileEnclosure.add_animal(reptile1)
        assert reptile1.get_name() not in reptileEnclosure.get_animalsenclosedlist()
        assert reptileEnclosure.get_current_capacity() == 0

    def test_incompatibleAnimal(self, reptileEnclosure, mammal1): # Test adding INCOMPATIBLE ANIMAL to enclosure
        with pytest.raises(ValueError):
            reptileEnclosure.add_animal(mammal1)
        assert mammal1.get_name() not in reptileEnclosure.get_animalsenclosedlist()
        assert reptileEnclosure.get_current_capacity() == 0

    def test_incompatibleEnvironment(self, reptileEnclosure, reptile1): # Test adding animal to INCOMPATIBLE ENVIRONMENT
        reptileEnclosure.set_environment("Savanna")
        with pytest.raises(ValueError):
            reptileEnclosure.add_animal(reptile1)
        assert reptile1.get_name() not in reptileEnclosure.get_animalsenclosedlist()
        assert reptileEnclosure.get_current_capacity() == 0

    def test_incompatibleSize(self, reptileEnclosure, reptile1): # Test adding animal to INCOMPATIBLE ENCLOSURE SIZE
        reptileEnclosure.set_size("Small")
        with pytest.raises(ValueError):
            reptileEnclosure.add_animal(reptile1)
        assert reptile1.get_name() not in reptileEnclosure.get_animalsenclosedlist()
        assert reptileEnclosure.get_current_capacity() == 0


    def test_maxCapacity(self, reptileEnclosure, reptile1): # Test animals cannot be added if at MAX capacity
        reptileEnclosure.set_current_capacity(5)
        with pytest.raises(ValueError):
            reptileEnclosure.add_animal(reptile1)
        assert reptile1.get_name() not in reptileEnclosure.get_animalsenclosedlist()
        assert reptileEnclosure.get_current_capacity() == 5

    def test_removingAnimal(self, reptileEnclosure, reptile1): # Test REMOVING animal and CAPACITY updates correctly
        reptileEnclosure.add_animal(reptile1)
        reptileEnclosure.remove_animal(reptile1)
        assert reptile1.get_name() not in reptileEnclosure.get_animalsenclosedlist()
        assert reptileEnclosure.get_current_capacity() == 0

    def test_removingAnimalNotInEnclosure(self, reptileEnclosure, reptile1): # Test REMOVING animals NOT in enclosure
        with pytest.raises(ValueError):
            reptileEnclosure.remove_animal(reptile1)

    def test_addingDuplicateAnimal(self, reptileEnclosure, reptile1): # Test adding DUPLICATE ANIMALS to enclosure
        reptileEnclosure.add_animal(reptile1)
        with pytest.raises(ValueError):
            reptileEnclosure.add_animal(reptile1)

    def test_addingInvalidObject(self, reptileEnclosure): # Test ADDING invalid objects
        with pytest.raises(TypeError):
            reptileEnclosure.add_animal("InvalidAnimal")
            reptileEnclosure.add_animal(3465)

    def test_removingInvalidObject(self, reptileEnclosure): # Test REMOVING invalid objects
        with pytest.raises(TypeError):
            reptileEnclosure.remove_animal("InvalidAnimal")
            reptileEnclosure.remove_animal(3465)

    def test_moveSickAnimal(self, reptileEnclosure, reptile1): # Test moving/removing a SICK animal as it is not allowed
        reptileEnclosure.add_animal(reptile1)
        reptile1.get_health().set_health_status("Sick")
        with pytest.raises(ValueError):
            reptileEnclosure.remove_animal(reptile1)
        assert reptile1.get_name() in reptileEnclosure.get_animalsenclosedlist()

    def test_moveUnderTreatmentAnimal(self, reptileEnclosure, reptile1): # Test moving/removing an animal UNDER TREATMENT as it is not allowed
        reptileEnclosure.add_animal(reptile1)
        reptile1.get_health().set_health_status("Under Treatment")
        with pytest.raises(ValueError):
            reptileEnclosure.remove_animal(reptile1)
        assert reptile1.get_name() in reptileEnclosure.get_animalsenclosedlist()
