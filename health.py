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
    # Defined class variables before __init__ as variables should be applied and used by all health objects.
    severity = ["Minor", "Mild", "Major", "Critical"]
    health_statuses = ["Healthy", "Sick", "Under Treatment"]
    health_issues = {"Nil": ["No Issues"],
                     "Injury": ["Broken Bone", "Fractured Bone", "Sprain", "Wound", "Bite", "Bruising"],
                     "Illness": ["Infection", "Parasites", "Hypothermia", "Hyperthermia", "Malnutrition", "Diabetes", "Arthritis"],
                     "Behavioural Concern": ["Aggression", "Anxiety", "Destruction", "Self-mutilation", "Territorial", "Appetite Loss"]} # Used dictionary to be able to store categories and values

    def __init__(self, date=None, health_issuecategory="Nil", health_issue="No Issues", issue_description="Nil", severity="Nil", treatment_notes="Nil", health_status="Healthy"):
        # Attributes which include data validation to ensure only valid inputs are passed in and set
        self.__date = date
        self.__health_issuecategory = health_issuecategory
        self.__health_issue = health_issue
        self.__health_status = health_status
        self.__issue_description = issue_description
        self.__severity = severity
        self.__treatment_notes = treatment_notes
        self.__health_history = []

        # Attribute validation
        if date is not None: # Sets date=None as default to prevent errors continuously returning
            if isinstance(date, str):
                self.set_date(date)
            else:
                raise TypeError("Date must be a string.")

        if isinstance(health_issuecategory, str) and isinstance(health_issue, str) and isinstance(issue_description, str) and isinstance(severity, str) and isinstance(treatment_notes, str):
            self.set_health_issue(health_issuecategory, health_issue, issue_description, severity, treatment_notes)
        else:
            raise TypeError("All inputs must be strings.")

        if isinstance(health_status, str):
            self.set_health_status(health_status)
        else:
            raise TypeError("Health Status must be a string.")

    # Getters for attributes
    def get_date(self):
        return self.__date

    def get_health_status(self):
        return self.__health_status

    def get_health_issue(self):
        return self.__health_issue

    def get_health_issuecategory(self):
        return self.__health_issuecategory

    def get_health_history(self):
        return self.__health_history

    def get_issue_description(self):
        return self.__issue_description

    def get_severity(self):
        return self.__severity

    def get_treatment_notes(self):
        return self.__treatment_notes


    # Setters for attributes
    def set_date(self, date):
        try:
            self.__date = datetime.strptime(date, "%d/%m/%Y").strftime("%d/%m/%Y") # Date time function utilised and converted into a string for readability purposes
        except ValueError:
            raise ValueError("Date must be in DD/MM/YYYY format.")

        # Code inspired by:
        # Anderson, A & Walia, S, Anish, 2024. How to convert a string to a datetime object in python. [Online] DigitalOcean
        # Available at: <https://www.digitalocean.com/community/tutorials/python-string-to-datetime-strptime>
        # [Accessed 6 November 2025]

    def set_health_status(self, health_status):
        if health_status in self.health_statuses:
            self.__health_status = health_status
        else:
            raise ValueError(f"Health Status must be selected from the following: {self.health_statuses}")

    def set_health_issue(self, health_issuecategory, health_issue, issue_description, severity, treatment_notes):
        if health_issuecategory in self.health_issues: # Validating that the health issue category is valid
            if health_issue in self.health_issues[health_issuecategory]: # If health issue is located within the health issue category assign attributes
                self.__health_issuecategory = health_issuecategory
                self.__health_issue = health_issue
                self.__issue_description = issue_description
                self.__treatment_notes = treatment_notes
                if severity in severity:
                    self.__severity = severity
                else:
                    raise ValueError(f"Severity must be selected from the following: {self.severity}")
            else:
                raise ValueError(f"Issue must be selected from the following: {self.health_issues[health_issuecategory]}")
        else:
            raise ValueError(f"Category must be selected from the following: {self.health_issues.keys()}")

    # Methods
    def update_healthissue(self, date, health_issuecategory, health_issue, issue_description, severity, treatment_notes, health_status): # Updates current health issue and appends previous health issue into health history
        if self.__health_issuecategory != "Nil": # Append previous health issue into medical record history
            self.__health_history.append([self.__date, self.__health_issuecategory, self.__health_issue, self.__issue_description, self.__severity, self.__treatment_notes, self.__health_status])
        self.set_date(date)
        self.set_health_issue(health_issuecategory, health_issue, issue_description, severity, treatment_notes)
        self.set_health_status(health_status)

    def generate_animalreport(self, animal_name, animal_classification, animal_species, animal_age): # Generates a health report for an individual animal
        print("------------------------")
        print("\033[1mHealth Report\033[0m")
        print("------------------------")
        print(f"\033[1mName:\033[0m {animal_name}")
        print(f"\033[1mClassification:\033[0m {animal_classification}")
        print(f"\033[1mSpecies:\033[0m {animal_species}")
        print(f"\033[1mAge:\033[0m {animal_age}")
        print("------------------------")
        print("\033[1mCurrent Health Status:\033[0m")
        print("----")
        print(f"Health Status: {self.__health_status}")
        print(f"Health Issue: \033[1mDate:\033[0m {self.__date} | \033[1m{self.__health_issuecategory}\033[0m- {self.__health_issue} | \033[1mDescription:\033[0m {self.__issue_description} | \033[1mSeverity:\033[0m {self.__severity} | \033[1mTreatment Notes:\033[0m {self.__treatment_notes}")
        print("------------------------")
        print("\033[1mPast Medical History:\033[0m")
        print("----")
        for healthRecord in self.__health_history:
            print(f" \033[1mDate:\033[0m {healthRecord[0]} | \033[1m{healthRecord[1]}\033[0m: {healthRecord[2]} | \033[1mDescription:\033[0m {healthRecord[3]} | \033[1mSeverity:\033[0m {healthRecord[4]} | \033[1mTreatment Notes:\033[0m {healthRecord[5]}\n")
        print("------------------------")
        # Code inspired by:
        # Kodeclik, 2025. How to bold text in python. [Online] Kodeclik.
        # Available at: <https://www.kodeclik.com/how-to-bold-text-in-python/>
        # [Accessed 6 November 2025].

    def __str__(self):
        return f"Health Profile has been successfully created.\n"