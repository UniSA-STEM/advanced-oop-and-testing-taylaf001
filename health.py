'''
File: health.py
Description: health.py contains code for the health management aspect of the zoo.
Author: Tayla Fontanabella
ID: Taylaf001
Username: Fonty005
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Health:
    health_Statuses = ["Healthy", "Sick", "Under Treatment"]
    health_Issues = {"Injuries": ["Broken Bone", "Fractured Bone", "Sprain", "Wound", "Bite", "Bruising"],
                     "Illnesses": ["Infection", "Parasites", "Hypothermia", "Hyperthermia", "Malnutrition", "Diabetes", "Arthritis"],
                     "Behavioural Concerns": ["Aggression", "Anxiety", "Destruction", "Self-mutilation", "Territorial", "Appetite Loss"]}

    def __init__(self, health_IssueCategory, health_Issue, health_Status):
        if isinstance(health_IssueCategory, str) and isinstance (health_Issue, str):
            self.set_health_Issue(health_IssueCategory, health_Issue)
        else:
            raise TypeError("Issue Category & Health Issue must be a string.")

        if isinstance(health_Status, str):
            self.set_health_Status(health_Status)
        else:
            raise TypeError("Health Status must be a string.")

    def set_health_Status(self, health_status):
        if health_status in self.health_Statuses:
            self.__health_Status = health_status
        else:
            raise ValueError(f"Health Status must be selected from the following: {self.health_Statuses}")

    def set_health_Issue(self, health_IssueCategory, health_Issue):
        if health_IssueCategory in self.health_Issues:
            if health_Issue in self.health_Issues[health_IssueCategory]:
                self.__health_IssueCategory = health_IssueCategory
                self.__health_Issue = health_Issue
            else:
                raise ValueError(f"Issue must be selected from the following: {self.health_Issues[category]}")
        else:
            raise ValueError(f"Category must be selected from the following: {self.health_Issues.keys()}")

    def add_HealthIssue(self, animal, health_Issue, health_Status):
        self.set_health_Issue(health_Issue)

    def generate_HealthReport(self, subject, ):