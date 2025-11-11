'''
File: test_zoo.py
Description: This file contains all tests for zoo.py
Author: Tayla Fontanabella
ID: taylaf001
Username: Fonty005
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from zoo import Zoo
from reptile import Reptile
from bird import Bird
from veterinarian import Veterinarian
from zookeeper import Zookeeper
from enclosure import Enclosure

class TestZoo:
    @pytest.fixture(autouse=True)  # Resets used IDs and set to auto use to automatically reset after each file use
    def reset_staffID(self):
        Zookeeper.used_staffID = set()
        Veterinarian.used_staffID = set()

    @pytest.fixture
    def zoo1(self):
        return Zoo("Zoo")

    @pytest.fixture
    def reptile1(self):
        return Reptile("Ed", "Reptile", "Snake", 4, "Carnivore", "Exotic", "Desert", "Medium", True)

    @pytest.fixture
    def bird1(self):
        return Bird("Mike", "Bird", "Macaw", 39, "Omnivore", "Avian", "Tropical", "Large", True)

    @pytest.fixture
    def vet1(self):
        return Veterinarian("Lily", 4872, "Veterinarian", "Avian")

    @pytest.fixture
    def zookeeper1(self):
        return Zookeeper("Andrew", 1637, "Zookeeper")

    @pytest.fixture
    def enclosure1(self):
        return Enclosure("Big Reptiles", "Medium", "Desert", "Reptile", 5)

    def test_zoo1(self, zoo1):
        assert isinstance(zoo1, Zoo)
        assert zoo1.get_name() == "Zoo"

    def test_raises(self):
        with pytest.raises(TypeError): # Incorrect NAME Type
            Zoo(456)

    def test_addEnclosure(self, zoo1, enclosure1): # Test adding an enclosure to zoo
        zoo1.add_enclosure(enclosure1)
        assert enclosure1 in zoo1.get_enclosures()

    def test_removeEnclosure(self, zoo1, enclosure1): # Test removing an enclosure from zoo
        zoo1.add_enclosure(enclosure1)
        zoo1.remove_enclosure(enclosure1)
        assert enclosure1 not in zoo1.get_enclosures()

    def test_addInvalidEnclosure(self, zoo1): # Add invalid enclosure types
        with pytest.raises(TypeError):
            zoo1.add_enclosure("Enclosure1")
        with pytest.raises(TypeError):
            zoo1.add_enclosure(25234)

    def test_removeInvalidEnclosure(self, zoo1, enclosure1): # Remove enclosure not in zoo
        with pytest.raises(ValueError):
            zoo1.remove_enclosure(enclosure1)

    def test_addAnimal(self, zoo1, enclosure1, reptile1): # Test adding animal to zoo and enclosure
        zoo1.add_animal(reptile1)
        assert reptile1 in zoo1.get_animals()
        zoo1.add_enclosure(enclosure1)
        assert enclosure1 in zoo1.get_enclosures()
        enclosure1.add_animal(reptile1)
        assert reptile1.get_name() in enclosure1.get_animalsenclosedlist()

    def test_removeAnimal(self, zoo1, enclosure1, reptile1): # Test removing animal from zoo and enclosure
        zoo1.add_animal(reptile1)
        zoo1.add_enclosure(enclosure1)
        enclosure1.add_animal(reptile1)
        enclosure1.remove_animal(reptile1)
        assert reptile1.get_name() not in enclosure1.get_animalsenclosedlist()
        zoo1.remove_animal(reptile1)
        assert reptile1 not in zoo1.get_animals()

    def test_addInvalidAnimal(self, zoo1): # Test adding an invalid animal
        with pytest.raises(TypeError):
            zoo1.add_animal(25234)
        with pytest.raises(TypeError):
            zoo1.add_animal("Monkey")

    def test_removeInvalidAnimal(self, zoo1): # Test removing an invalid animal
        with pytest.raises(TypeError):
            zoo1.remove_animal(25234)
        with pytest.raises(TypeError):
            zoo1.remove_animal("Monkey")

    def test_addStaff(self, zoo1, vet1, zookeeper1): # Test adding staff to zoo
        zoo1.add_staff(vet1)
        assert vet1 in zoo1.get_staff()
        zoo1.add_staff(zookeeper1)
        assert zookeeper1 in zoo1.get_staff()

    def test_removeStaff(self, zoo1, vet1, zookeeper1): # Test removing staff to zoo
        zoo1.add_staff(vet1)
        zoo1.remove_staff(vet1)
        assert vet1 not in zoo1.get_staff()
        zoo1.add_staff(zookeeper1)
        zoo1.remove_staff(zookeeper1)
        assert zookeeper1 not in zoo1.get_staff()

    def test_addInvalidStaff(self, zoo1): # Test adding invalid staff
        with pytest.raises(TypeError):
            zoo1.add_staff(25234)
        with pytest.raises(TypeError):
            zoo1.add_staff("John")

    def test_removeInvalidStaff(self, zoo1): # Test removing invalid staff
        with pytest.raises(TypeError):
            zoo1.remove_staff(25234)
        with pytest.raises(TypeError):
            zoo1.remove_staff("John")

    def test_addDuplicateAnimal(self, zoo1, reptile1): # Test adding duplicate animals
        zoo1.add_animal(reptile1)
        with pytest.raises(ValueError):
            zoo1.add_animal(reptile1)

    def test_addDuplicateStaff(self, zoo1, zookeeper1): # Test adding duplicate staff
        zoo1.add_staff(zookeeper1)
        with pytest.raises(ValueError):
            zoo1.add_staff(zookeeper1)

    def test_addDuplicateEnclosure(self, zoo1, enclosure1): # Test adding duplicate enclosures
        zoo1.add_enclosure(enclosure1)
        with pytest.raises(ValueError):
            zoo1.add_enclosure(enclosure1)

    def test_removeAnimalNotInZoo(self, zoo1, reptile1): # Test removing animals not added into zoo
        with pytest.raises(ValueError):
            zoo1.remove_animal(reptile1)

    def test_removeStaffNotInZoo(self, zoo1, zookeeper1): # Test removing staff not added into zoo
        with pytest.raises(ValueError):
            zoo1.remove_staff(zookeeper1)

    def test_removeEnclosureNotInZoo(self, zoo1, enclosure1): # Test removing enclosure not added into zoo
        with pytest.raises(ValueError):
            zoo1.remove_enclosure(enclosure1)

