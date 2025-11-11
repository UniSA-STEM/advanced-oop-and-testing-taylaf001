'''
File: test_health.py
Description: This file contains all tests for health.py
Author: Tayla Fontanabella
ID: taylaf001
Username: Fonty005
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from health import Health
from bird import Bird

class TestHealth:

    @pytest.fixture
    def health1(self):
        return Health("04/10/2025", "Behavioural Concern", "Territorial", "Territorial of shelter", "Minor", "Observation - no treatment necessary", "Healthy")

    @pytest.fixture
    def bird1(self):
        return Bird("Mike", "Bird", "Macaw", 39, "Omnivore", "Avian", "Tropical", "Large", True)

    def test_health1(self, health1):
        assert isinstance(health1, Health)
        assert health1.get_date() == "04/10/2025"
        assert health1.get_health_issuecategory() == "Behavioural Concern"
        assert health1.get_health_issue() == "Territorial"
        assert health1.get_issue_description() == "Territorial of shelter"
        assert health1.get_severity() == "Minor"
        assert health1.get_treatment_notes() == "Observation - no treatment necessary"
        assert health1.get_health_status() == "Healthy"

    def test_raises(self):
        with pytest.raises(ValueError): # Incorrect DATE Type
            Health("10-04-25", "Behavioural Concern", "Territorial", "Territorial of shelter", "Minor","Observation - no treatment necessary", "Healthy")

        with pytest.raises(TypeError): # Incorrect Health Issue Category Type
            Health("04/10/2025", 345, "Territorial", "Territorial of shelter", "Minor","Observation - no treatment necessary", "Healthy")
        with pytest.raises(ValueError): # Incorrect Health Issue Category Value
            Health("04/10/2025", "Bad behaviour", "Territorial", "Territorial of shelter", "Minor","Observation - no treatment necessary", "Healthy")

        with pytest.raises(TypeError): # Incorrect health issue type
            Health("04/10/2025", "Behavioural Concern", 345, "Territorial of shelter", "Minor","Observation - no treatment necessary", "Healthy")
        with pytest.raises(ValueError): # Incorrect health issue value

            Health("04/10/2025", "Behavioural Concern", "Wont leave shelter", "Territorial of shelter", "Minor","Observation - no treatment necessary", "Healthy")
        with pytest.raises(TypeError): # Incorrect issue description type
            Health("04/10/2025", "Behavioural Concern", "Territorial", 456, "Minor","Observation - no treatment necessary", "Healthy")

        with pytest.raises(TypeError): # Incorrect severity type
            Health("04/10/2025", "Behavioural Concern", "Territorial", "Territorial of shelter", 3465,"Observation - no treatment necessary", "Healthy")
        with pytest.raises(ValueError): # Incorrect severity value
            Health("04/10/2025", "Behavioural Concern", "Territorial", "Territorial of shelter", "Not bad", "Observation - no treatment necessary", "Healthy")

        with pytest.raises(TypeError): # Incorrect treatment note type
            Health("04/10/2025", "Behavioural Concern", "Territorial", "Territorial of shelter", "Minor",456456, "Healthy")

        with pytest.raises(TypeError): # Incorrect health status type
            Health("04/10/2025", "Behavioural Concern", "Territorial", "Territorial of shelter", "Minor", "Observation - no treatment necessary", 5464)
        with pytest.raises(ValueError): # Incorrect health status value
            Health("04/10/2025", "Behavioural Concern", "Territorial", "Territorial of shelter", "Minor", "Observation - no treatment necessary", "OK")

    def test_updateHealthHistory(self, health1): # Test that health history updates correctly
        health1.update_healthissue("05/11/2025", "Injury", "Sprain", "Sprained wing", "Minor", "No treatment necessary", "Healthy")
        health1.update_healthissue("11/11/2025", "Illness", "Infection", "Minor toe infection", "Minor", "Mike given 0.5ml dose of antibiotics", "Under Treatment") # CURRENT HEALTH ISSUE (DOES NOT APPEND INTO HEALTH HISTORY UNTIL A NEW ONE IS ADDED AFTER THIS)
        assert len(health1.get_health_history()) == 2
        assert health1.get_health_history()[0][0] == "04/10/2025"
        assert health1.get_health_history()[0][1] == "Behavioural Concern"
        assert health1.get_health_history()[0][2] == "Territorial"
        assert health1.get_health_history()[0][3] == "Territorial of shelter"
        assert health1.get_health_history()[0][4] == "Minor"
        assert health1.get_health_history()[0][5] == "Observation - no treatment necessary"
        assert health1.get_health_history()[0][6] == "Healthy"
        assert health1.get_health_history()[1][0] == "05/11/2025"
        assert health1.get_health_history()[1][1] == "Injury"
        assert health1.get_health_history()[1][2] == "Sprain"
        assert health1.get_health_history()[1][3] == "Sprained wing"
        assert health1.get_health_history()[1][4] == "Minor"
        assert health1.get_health_history()[1][5] == "No treatment necessary"
        assert health1.get_health_history()[1][6] == "Healthy"

    def test_generateHealthReport(self, health1, bird1): # Test generating a health report
        healthReport = health1.generate_animalreport(bird1.get_name(), bird1.get_classification(), bird1.get_species(), bird1.get_age())
        assert bird1.get_name() in healthReport
        assert bird1.get_classification() in healthReport
        assert bird1.get_species() in healthReport
        assert str(bird1.get_age()) in healthReport
