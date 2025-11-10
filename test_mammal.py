'''
File: test_mammal.py
Description: This file contains all tests for mammal.py
Author: Tayla Fontanabella
ID: taylaf001
Username: Fonty005
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from mammal import Mammal

class TestMammal:
    @pytest.fixture
    def mammal1(self):
        return Mammal("Ellie", "Mammal", "Elephant", 14, "Herbivore", "Mammal", "Savanna", "Large", "None")

    def test_mammal1(self, mammal1): # Testing all attributes have been assigned correctly
        assert isinstance(mammal1, Mammal)
        assert mammal1.get_name() == "Ellie"
        assert mammal1.get_classification() == "Mammal"
        assert mammal1.get_species() == "Elephant"
        assert mammal1.get_age() == 14
        assert mammal1.get_dietary_requirements() =="Herbivore"
        assert mammal1.get_specialisation_needed() == "Mammal"
        assert mammal1.get_preferred_environment() == "Savanna"
        assert mammal1.get_preferred_space() == "Large"
        assert mammal1.get_fur_type() == "None"

    def test_raises(self):
        with pytest.raises(TypeError): # Testing non string and invalid attribute inputs
            Mammal(7, "Mammmdryfmal", "Elephant", "14", "Plants", 80, "None", 100, 9)

    def test_healthReport(self, mammal1): # Health report generation test
        mammal1.health_report()

    def test_makingSounds(self, mammal1): # Making sounds test
        mammal1.making_sounds()

    def test_eating(self, mammal1): # Eating test
        mammal1.eating()

    def test_sleeping(self, mammal1): # Sleeping test
        mammal1.sleeping()

    def test_socialise(self, mammal1): # Socialise test
        mammal1.socialise()

    def test_nurseOffspring(self, mammal1): # Nurse offspring test
        mammal1.nurse_offspring()

    def test_play(self, mammal1): # Play test
        mammal1.play()
