'''
File: test_veterinarian.py
Description: This file contains all tests for veterinarian.py
Author: Tayla Fontanabella
ID: taylaf001
Username: Fonty005
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from veterinarian import Veterinarian
from bird import Bird
from mammal import Mammal

class TestVet:
    @pytest.fixture(autouse=True) # Resets used IDs and set to auto use to automatically reset after each file use
    def reset_staffID(self):
        Veterinarian.used_staffID = set()

    @pytest.fixture
    def vet1(self):
        return Veterinarian("Lily", 4872, "Veterinarian", "Avian")

    @pytest.fixture
    def mammal1(self):
        return Mammal("Ellie", "Mammal", "Elephant", 14, "Herbivore", "Mammal", "Savanna", "Large", "None")

    @pytest.fixture
    def bird1(self):
        return Bird("Mike", "Bird", "Macaw", 39, "Omnivore", "Avian", "Tropical", "Large", True)

    def test_vet1(self, vet1):
        assert isinstance(vet1, Veterinarian)
        assert vet1.get_name() == "Lily"
        assert vet1.get_staffID() == 4872
        assert vet1.get_role() == "Veterinarian"
        assert vet1.get_specialisation() == "Avian"

    def test_raises(self):
        with pytest.raises(TypeError): # NAME - Incorrect Type
            Veterinarian(345, 4874, "Veterinarian", "Avian")

        with pytest.raises(TypeError): # STAFF ID - Incorrect Type
            Veterinarian("Lily", "4876", "Veterinarian", "Avian")

        with pytest.raises(ValueError): # STAFF ID - Incorrect Value (<1000)
            Veterinarian("Lily", 999, "Veterinarian", "Avian")

        with pytest.raises(ValueError): # STAFF ID - Incorrect Value (>9999)
            Veterinarian("Lily", 10200, "Veterinarian", "Avian")

        with pytest.raises(TypeError): # ROLE - Incorrect Type
            Veterinarian("Lily", 4562, 345, "Avian")

        with pytest.raises(ValueError): # ROLE - Incorrect Value
            Veterinarian("Lily", 6784, "Admin", "Avian")

        with pytest.raises(TypeError): # SPECIALISATION - Incorrect Type
            Veterinarian("Lily", 1233, "Veterinarian", 345)

        with pytest.raises(ValueError): # SPECIALISATION - Incorrect Value
            Veterinarian("Lily", 8999, "Veterinarian", "Bird")

    def test_assignIncorrectAnimal(self, vet1, mammal1): # Test setting INCORRECT animal
        with pytest.raises(ValueError):
            vet1.assign_animal(mammal1)

    def test_assignCorrectAnimal(self, vet1, bird1): # Test setting CORRECT animal
        vet1.assign_animal(bird1)
        assert bird1 in vet1.get_assigned_animals()

    def test_removeAnimal(self, vet1, bird1): # Test REMOVING animal
        vet1.assign_animal(bird1)
        assert bird1 in vet1.get_assigned_animals()
        vet1.unassign_animal(bird1)
        assert bird1 not in vet1.get_assigned_animals()

    def test_assignInvalidObject(self, vet1):  # Test ADDING invalid objects
        with pytest.raises(TypeError):
            vet1.assign_animal("InvalidAnimal")
            vet1.assign_animal(3465)

    def test_removingInvalidObject(self, vet1):  # Test REMOVING invalid objects
        with pytest.raises(TypeError):
            vet1.unassign_animal("InvalidAnimal")
            vet1.unassign_animal(3465)

    def test_assignDuplicateAnimal(self, vet1, bird1): # Test ADDING duplicate animals
        vet1.assign_animal(bird1)
        with pytest.raises(ValueError):
            vet1.assign_animal(bird1)

    def test_healthCheck(self, vet1, bird1): # Test performing health check on valid animal
        vet1.assign_animal(bird1)
        assert bird1 in vet1.get_assigned_animals()
        vet1.perform_healthcheck(bird1)

    def test_healthCheckInvalidAnimal(self, vet1, mammal1): # Test performing health check on INVALID animals
        with pytest.raises(ValueError):
            vet1.perform_healthcheck(mammal1)

    def test_healthCheckInvalidObject(self, vet1):  # Test performing health check on INVALID OBJECTS
        with pytest.raises(TypeError):
            vet1.perform_healthcheck("InvalidAnimal")
        with pytest.raises(TypeError):
            vet1.perform_healthcheck(345)



