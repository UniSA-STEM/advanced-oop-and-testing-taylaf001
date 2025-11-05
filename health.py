'''
File: health.py
Description: health.py contains code for the health management aspect of the zoo.
Author: Tayla Fontanabella
ID: Taylaf001
Username: Fonty005
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Health:
    def __init__(self, health_Issue, health_Status):
        health_Statuses = ["Healthy", "Sick", "Under Treatment"]
        health_Issues = {"Injuries", ("Broken Bone", "Fractured Bone", "Sprain", "Wound", "Bite", "Bruising"),
                         "Illnesses", ("Infection", "Parasites", "Hypothermia", "Hyperthermia", "Malnutrition", "Diabetes", "Arthritis"),
                         "Behavioural Concerns", ("Aggression", "Anxiety", "Destruction", "Self-mutilation", "Territorial", "Appetite Loss")}