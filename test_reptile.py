'''
File: test_reptile.py
Description: This file contains all tests for reptile.py
Author: Tayla Fontanabella
ID: taylaf001
Username: Fonty005
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from reptile import Reptile

class TestReptile:
    @pytest.fixture
    def reptile1(self):
        return Reptile("Ed", "Reptile", "Snake", 4, "Carnivore", "Exotic", "Desert", "Medium",True)

    def test_reptile1(self, reptile1): # Testing all attributes have been assigned correctly
        assert isinstance(reptile1, Reptile)
        assert reptile1.get_name() == "Ed"
        assert reptile1.get_classification() == "Reptile"
        assert reptile1.get_species() == "Snake"
        assert reptile1.get_age() == 4
        assert reptile1.get_dietary_requirements() == "Carnivore"
        assert reptile1.get_specialisation_needed() == "Exotic"
        assert reptile1.get_preferred_environment() == "Desert"
        assert reptile1.get_preferred_space() == "Medium"
        assert reptile1.get_venomous() == True

    def test_raises(self):
        with pytest.raises(TypeError):  # NAME - Incorrect Type
            Reptile(653, "Reptile", "Snake", 4, "Carnivore", "Exotic", "Desert", "Medium",True)

        with pytest.raises(ValueError):  # CLASSIFICATION - Incorrect Value
            Reptile("Ed", "Scaly Thing", "Snake", 4, "Carnivore", "Exotic", "Desert", "Medium",True)

        with pytest.raises(TypeError):  # CLASSIFICATION - Incorrect Type
            Reptile("Ed", 345, "Snake", 4, "Carnivore", "Exotic", "Desert", "Medium",True)

        with pytest.raises(TypeError):  # SPECIES - Incorrect Type
            Reptile("Ed", "Reptile", 456, 4, "Carnivore", "Exotic", "Desert", "Medium",True)

        with pytest.raises(TypeError):  # AGE - Incorrect Type
            Reptile("Ed", "Reptile", "Snake", "4", "Carnivore", "Exotic", "Desert", "Medium",True)

        with pytest.raises(TypeError):  # DIETARY REQUIREMENTS - Incorrect Type
            Reptile("Ed", "Reptile", "Snake", 4, 453, "Exotic", "Desert", "Medium",True)

        with pytest.raises(ValueError):  # DIETARY REQUIREMENTS - Incorrect Value
            Reptile("Ed", "Reptile", "Snake", 4, "Meat Eater", "Exotic", "Desert", "Medium",True)

        with pytest.raises(TypeError):  # SPECIALISATION NEEDED - Incorrect Type
            Reptile("Ed", "Reptile", "Snake", 4, "Carnivore", 456, "Desert", "Medium",True)

        with pytest.raises(ValueError):  # SPECIALISATION NEEDED - Incorrect Value
            Reptile("Ed", "Reptile", "Snake", 4, "Carnivore", "Reptile Vet", "Desert", "Medium",True)

        with pytest.raises(TypeError):  # PREFERRED ENVIRONMENT - Incorrect Type
            Reptile("Ed", "Reptile", "Snake", 4, "Carnivore", "Exotic", 345, "Medium",True)

        with pytest.raises(ValueError):  # PREFERRED ENVIRONMENT - Incorrect Value
            Reptile("Ed", "Reptile", "Snake", 4, "Carnivore", "Exotic", "On a Rock", "Medium",True)

        with pytest.raises(TypeError):  # PREFERRED SPACE - Incorrect Type
            Reptile("Ed", "Reptile", "Snake", 4, "Carnivore", "Exotic", "Desert", 3645,True)

        with pytest.raises(ValueError):  # PREFERRED SPACE - Incorrect Value
            Reptile("Ed", "Reptile", "Snake", 4, "Carnivore", "Exotic", "Desert", "Tiny",True)

        with pytest.raises(TypeError): # IS VENOMOUS - Incorrect Type
            Reptile("Ed", "Reptile", "Snake", 4, "Carnivore", "Exotic", "Desert", "Medium", 456)


    def test_healthReport(self, reptile1): # Health report generation test
        reptile1.health_report()

    def test_makingSounds(self, reptile1): # Making sounds test
        reptile1.making_sounds()

    def test_eating(self, reptile1): # Eating test
        reptile1.eating()

    def test_sleeping(self, reptile1): # Sleeping test
        reptile1.sleeping()

    def test_shedSkin(self, reptile1):
        reptile1.shed_skin()

    def test_baskInSun(self, reptile1):
        reptile1.bask_insun()

    def test_hunt(self, reptile1):
        reptile1.hunt()