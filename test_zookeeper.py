'''
File: test_zookeeper.py
Description: This file contains all tests for zookeeper.py
Author: Tayla Fontanabella
ID: taylaf001
Username: Fonty005
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from zookeeper import Zookeeper
from mammal import Mammal
from enclosure import Enclosure

class TestZookeeper:
    @pytest.fixture(autouse=True) # Resets used IDs and set to auto use to automatically reset after each file use
    def reset_staffID(self):
        Zookeeper.used_staffID = set()

    @pytest.fixture
    def zookeeper1(self):
        return Zookeeper("Andrew", 1637, "Zookeeper")

    @pytest.fixture
    def mammal1(self):
        return Mammal("Ellie", "Mammal", "Elephant", 14, "Herbivore", "Mammal", "Savanna", "Large", "None")

    @pytest.fixture
    def enclosure1(self):
        return Enclosure("Large Mammals", "Large", "Savanna", "Mammal", 10)

    def test_zookeeper1(self, zookeeper1):
        assert isinstance(zookeeper1, Zookeeper)
        assert zookeeper1.get_name() == "Andrew"
        assert zookeeper1.get_staffID() == 1637
        assert zookeeper1.get_role() == "Zookeeper"

    def test_raises(self):
        with pytest.raises(TypeError): # NAME - Incorrect Type
            Zookeeper(546, 1637, "Zookeeper")

        with pytest.raises(TypeError): # STAFF ID - Incorrect Type
            Zookeeper("Andrew", "1637", "Zookeeper")

        with pytest.raises(ValueError): # STAFF ID - Incorrect Value (<1000)
            Zookeeper("Andrew", 873, "Zookeeper")

        with pytest.raises(ValueError): # STAFF ID - Incorrect Value (>9999)
            Zookeeper("Andrew", 34569, "Zookeeper")

        with pytest.raises(TypeError): # ROLE - Incorrect Type
            Zookeeper("Andrew", 1637, 456568)

        with pytest.raises(ValueError): # ROLE - Incorrect Value
            Zookeeper("Andrew", 1637, "Animal Assistant")

    def test_AssignEnclosure(self, enclosure1, zookeeper1): # Test assigning enclosure to zookeeper
        zookeeper1.assign_enclosure(enclosure1)
        assert enclosure1 in zookeeper1.get_assigned_enclosures()

    def test_AssignDuplicateEnclosure(self, enclosure1, zookeeper1): # Test assigning DUPLICATE enclosure
        zookeeper1.assign_enclosure(enclosure1)
        with pytest.raises(ValueError):
            zookeeper1.assign_enclosure(enclosure1)

    def test_AssignInvalidEnclosure(self, zookeeper1): # Test assigning INVALID object to zookeeper
        with pytest.raises(TypeError):
            zookeeper1.assign_enclosure("Enclosure1")
        with pytest.raises(TypeError):
            zookeeper1.assign_enclosure(3454)

    def test_unassignEnclosure(self, enclosure1, zookeeper1): # Test unassigning enclosure to zookeeper
        zookeeper1.assign_enclosure(enclosure1)
        zookeeper1.unassign_enclosure(enclosure1)
        assert enclosure1 not in zookeeper1.get_assigned_enclosures()

    def test_unassignEnclosureNotAssigned(self, enclosure1, zookeeper1): # Test unassigning enclosure not assigned
        with pytest.raises(ValueError):
            zookeeper1.unassign_enclosure(enclosure1)
        assert enclosure1 not in zookeeper1.get_assigned_enclosures()

    def test_feedAnimal(self, zookeeper1): # Test invalid input
        with pytest.raises(TypeError):
            zookeeper1.feed_animal("Mammal")

    def test_cleanEnclosure(self, zookeeper1): # Test invalid input
        with pytest.raises(TypeError):
            zookeeper1.clean_enclosure("Enclosure1")


