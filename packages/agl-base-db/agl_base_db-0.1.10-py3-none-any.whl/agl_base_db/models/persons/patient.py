from .person import Person
from django import forms
from django.forms import DateInput
from rest_framework import serializers

class Patient(Person):
    """
    A class representing a patient.

    Attributes inhereted from Person:
        first_name (str): The first name of the patient.
        last_name (str): The last name of the patient.
        dob (datetime.date): The date of birth of the patient.
        gender (str): The gender of the patient.
        email (str): The email address of the patient.
        phone (str): The phone number of the patient.

    """

    def __str__(self):
        return self.first_name + " " + self.last_name + " (" + str(self.dob) + ")"
    
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'dob': DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
