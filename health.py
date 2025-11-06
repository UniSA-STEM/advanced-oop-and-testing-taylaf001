'''
File: health.py
Description: health.py contains code for the health management aspect of the zoo.
Author: Tayla Fontanabella
ID: Taylaf001
Username: Fonty005
This is my own work as defined by the University's Academic Integrity Policy.
'''
from datetime import datetime

class Health:
    severity = ["Minor", "Mild", "Major", "Critical"]
    health_Statuses = ["Healthy", "Sick", "Under Treatment"]
    health_Issues = {"Nil": ["No Issues"],
                     "Injury": ["Broken Bone", "Fractured Bone", "Sprain", "Wound", "Bite", "Bruising"],
                     "Illness": ["Infection", "Parasites", "Hypothermia", "Hyperthermia", "Malnutrition", "Diabetes", "Arthritis"],
                     "Behavioural Concern": ["Aggression", "Anxiety", "Destruction", "Self-mutilation", "Territorial", "Appetite Loss"]}

    def __init__(self, date=None, health_IssueCategory="Nil", health_Issue="No Issues", issue_Description="Nil", severity="Nil", treatment_notes="Nil", health_Status="Healthy"):
        self.__date = date
        self.__health_IssueCategory = health_IssueCategory
        self.__health_Issue = health_Issue
        self.__health_Status = health_Status
        self.__issue_Description = issue_Description
        self.__severity = severity
        self.__treatment_notes = treatment_notes
        self.__health_History = []

        # Attribute validation
        if date is not None: # Sets date=None as default to prevent type errors continuously returning
            if isinstance(date, str):
                    self.set_date(date)
            else:
                raise TypeError("Date must be a string.")

        if isinstance(health_IssueCategory, str) and isinstance(health_Issue, str) and isinstance(issue_Description, str) and isinstance(severity, str) and isinstance(treatment_notes, str):
            self.set_health_Issue(health_IssueCategory, health_Issue, issue_Description, severity, treatment_notes)
        else:
            raise TypeError("Issue Category & Health Issue must be a string.")

        if isinstance(health_Status, str):
            self.set_health_Status(health_Status)
        else:
            raise TypeError("Health Status must be a string.")

    # Getters for attributes

    def get_date(self):
        return self.__date

    def get_health_Status(self):
        return self.__health_Status

    def get_health_Issue(self):
        return self.__health_Issue

    def get_health_IssueCategory(self):
        return self.__health_IssueCategory

    def get_health_History(self):
        return self.__health_History

    def get_issue_Description(self):
        return self.__issue_Description

    def get_severity(self):
        return self.__severity

    def get_treatment_notes(self):
        return self.__treatment_notes


    # Setters for attributes

    def set_date(self, date):
        try:
            self.__date = datetime.strptime(date, "%d/%m/%Y").strftime("%d/%m/%Y") # Date time function utilised and converted into a string for readability purposes
        except:
            raise TypeError("Date must be in DD/MM/YYYY format.")

    def set_health_Status(self, health_status):
        if health_status in self.health_Statuses:
            self.__health_Status = health_status
        else:
            raise ValueError(f"Health Status must be selected from the following: {self.health_Statuses}")

    def set_health_Issue(self, health_IssueCategory, health_Issue, issue_Description, severity, treatment_notes):
        if health_IssueCategory in self.health_Issues:
            if health_Issue in self.health_Issues[health_IssueCategory]:
                self.__health_IssueCategory = health_IssueCategory
                self.__health_Issue = health_Issue
                self.__issue_Description = issue_Description
                self.__treatment_notes = treatment_notes
                if severity in severity:
                    self.__severity = severity
                else:
                    raise ValueError(f"Severity must be selected from the following: {self.severity}")
            else:
                raise ValueError(f"Issue must be selected from the following: {self.health_Issues[health_IssueCategory]}")
        else:
            raise ValueError(f"Category must be selected from the following: {self.health_Issues.keys()}")

    # Methods
    def update_HealthIssue(self, date, health_IssueCategory, health_Issue, issue_Description, severity, treatment_notes, health_Status):
        if self.__health_IssueCategory != "Nil": # Append previous health issue into medical record history
            self.__health_History.append([self.__date, self.__health_IssueCategory, self.__health_Issue, self.__issue_Description, self.__severity, self.__treatment_notes, self.__health_Status])
        self.set_date(date)
        self.set_health_Issue(health_IssueCategory, health_Issue, issue_Description, severity, treatment_notes)
        self.set_health_Status(health_Status)

    def generate_AnimalReport(self, animal_Name, animal_Classification, animal_Species, animal_Age):
        print("------------------------")
        print("\033[1mHealth Report\033[0m")
        print("------------------------")
        print(f"\033[1mName:\033[0m {animal_Name}")
        print(f"\033[1mClassification:\033[0m {animal_Classification}")
        print(f"\033[1mSpecies:\033[0m {animal_Species}")
        print(f"\033[1mAge:\033[0m {animal_Age}")
        print("------------------------")
        print("\033[1mCurrent Health Status:\033[0m")
        print("----")
        print(f"Health Status: {self.__health_Status}")
        print(f"Health Issue: \033[1mDate:\033[0m {self.__date} | \033[1m{self.__health_IssueCategory}\033[0m- {self.__health_Issue} | \033[1mDescription:\033[0m {self.__issue_Description} | \033[1mSeverity:\033[0m {self.__severity} | \033[1mTreatment Notes:\033[0m {self.__treatment_notes}")
        print("------------------------")
        print("\033[1mPast Medical History:\033[0m")
        print("----")
        for healthRecord in self.__health_History:
            print(f" \033[1mDate:\033[0m {healthRecord[0]} | \033[1m{healthRecord[1]}\033[0m: {healthRecord[2]} | \033[1mDescription:\033[0m {healthRecord[3]} | \033[1mSeverity:\033[0m {healthRecord[4]} | \033[1mTreatment Notes:\033[0m {healthRecord[5]}\n")
        print("------------------------")