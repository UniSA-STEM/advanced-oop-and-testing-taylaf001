from bird import Bird

class TestBird:
    @pytest.fixture
    def bird1(self):
        return Bird("Mike", "Bird", "Macaw", 39, "Omnivore", "Avian", "Forest", "Large", True)
