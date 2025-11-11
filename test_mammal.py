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
        with pytest.raises(TypeError):  # NAME - Incorrect Type
            Mammal(345, "Mammal", "Elephant", 14, "Herbivore", "Mammal", "Savanna", "Large", "None")

        with pytest.raises(ValueError):  # CLASSIFICATION - Incorrect Value
            Mammal("Ellie", "Elephant", "Elephant", 14, "Herbivore", "Mammal", "Savanna", "Large", "None")

        with pytest.raises(TypeError):  # CLASSIFICATION - Incorrect Type
            Mammal("Ellie", 345, "Elephant", 14, "Herbivore", "Mammal", "Savanna", "Large", "None")

        with pytest.raises(TypeError):  # SPECIES - Incorrect Type
            Mammal("Ellie", "Mammal", 8678, 14, "Herbivore", "Mammal", "Savanna", "Large", "None")

        with pytest.raises(TypeError):  # AGE - Incorrect Type
            Mammal("Ellie", "Mammal", "Elephant", "14", "Herbivore", "Mammal", "Savanna", "Large", "None")

        with pytest.raises(TypeError):  # DIETARY REQUIREMENTS - Incorrect Type
            Mammal("Ellie", "Mammal", "Elephant", 14, 354, "Mammal", "Savanna", "Large", "None")

        with pytest.raises(ValueError):  # DIETARY REQUIREMENTS - Incorrect Value
            Mammal("Ellie", "Mammal", "Elephant", 14, "Plants", "Mammal", "Savanna", "Large", "None")

        with pytest.raises(TypeError):  # SPECIALISATION NEEDED - Incorrect Type
            Mammal("Ellie", "Mammal", "Elephant", 14, "Herbivore", 345, "Savanna", "Large", "None")

        with pytest.raises(ValueError):  # SPECIALISATION NEEDED - Incorrect Value
            Mammal("Ellie", "Mammal", "Elephant", 14, "Herbivore", "Elephant Vet", "Savanna", "Large", "None")

        with pytest.raises(TypeError):  # PREFERRED ENVIRONMENT - Incorrect Type
            Mammal("Ellie", "Mammal", "Elephant", 14, "Herbivore", "Mammal", 567, "Large", "None")

        with pytest.raises(ValueError):  # PREFERRED ENVIRONMENT - Incorrect Value
            Mammal("Ellie", "Mammal", "Elephant", 14, "Herbivore", "Mammal", "Arid", "Large", "None")

        with pytest.raises(TypeError):  # PREFERRED SPACE - Incorrect Type
            Mammal("Ellie", "Mammal", "Elephant", 14, "Herbivore", "Mammal", "Savanna", 54363, "None")

        with pytest.raises(ValueError):  # PREFERRED SPACE - Incorrect Value
            Mammal("Ellie", "Mammal", "Elephant", 14, "Herbivore", "Mammal", "Savanna", "Huge Plains", "None")

        with pytest.raises(TypeError):  # FUR TYPE - Incorrect Type
            Mammal("Ellie", "Mammal", "Elephant", 14, "Herbivore", "Mammal", "Savanna", "Large", 456)

        with pytest.raises(ValueError):  # FUR TYPE - Incorrect Value
            Mammal("Ellie", "Mammal", "Elephant", 14, "Herbivore", "Mammal", "Savanna", "Large", "Stubble")

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
