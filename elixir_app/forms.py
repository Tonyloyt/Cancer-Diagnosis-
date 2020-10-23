from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import PatientDetails
from .models import Insert




class SavePatientDetails(forms.ModelForm):
    class Meta:
        model = PatientDetails
        fields = ['cardid', 'age', 'blood','gender', 'phone','address']

#creating patient form
patient_form = SavePatientDetails()

class UploadImage(forms.ModelForm):
    class Meta:
        model = Insert
        fields = ['filepaths','filename','upload_date']
        
    





