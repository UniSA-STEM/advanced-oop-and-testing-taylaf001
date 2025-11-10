'''
File: test_bird.py
Description: This file contains all tests for bird.py
Author: Tayla Fontanabella
ID: taylaf001
Username: Fonty005
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from bird import Bird

class TestBird:
    @pytest.fixture
    def bird1(self):
        return Bird("Mike", "Bird", "Macaw", 39, "Omnivore", "Avian", "Tropical", "Large", True)

    def test_bird1(self, bird1): # Testing all attributes have been assigned correctly
        assert isinstance(bird1, Bird)
        assert bird1.get_name() == "Mike"
        assert bird1.get_classification() == "Bird"
        assert bird1.get_species() == "Macaw"
        assert bird1.get_age() == 39
        assert bird1.get_dietary_requirements() == "Omnivore"
        assert bird1.get_specialisation_needed() == "Avian"
        assert bird1.get_preferred_environment() == "Tropical"
        assert bird1.get_preferred_space() == "Large"
        assert bird1.get_can_fly() == True

    def test_raises(self):
        with pytest.raises(TypeError): # Testing non string and invalid attribute inputs
            Bird(9, "Birdyyyy", "idk", "25243", "Meat", 80, "Desert", 100, 2)

    def test_healthReport(self, bird1): # Health report generation test
        bird1.health_report()

    def test_makingSounds(self, bird1): # Making sounds test
        bird1.making_sounds()

    def test_eating(self, bird1): # Eating test
        bird1.eating()

    def test_sleeping(self, bird1): # Sleeping test
        bird1.sleeping()

    def test_fly(self, bird1): # Sleeping test
        bird1.fly()

    def test_preenFeathers(self, bird1): # Preen feathers test
        bird1.preen_feathers()

    def test_buildNest(self, bird1): # Build nest test
        bird1.build_nest()

    def test_layEgg(self, bird1): # Lay egg test
        bird1.lay_egg()