from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import PatientDetails




class SavePatientDetails(forms.ModelForm):
    class Meta:
        model = PatientDetails
        fields = ['cardid', 'age', 'blood','gender', 'phone','address']

#creating patient form
patient_form = SavePatientDetails()

class UploadImage(forms.Form):
    filename = forms.FileField(max_length=200, widget=(forms.FileInput(attrs={'class': 'form-control input-file'})))





