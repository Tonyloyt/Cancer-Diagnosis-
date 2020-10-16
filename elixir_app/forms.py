from django import forms
from django.forms import ModelForm
from .models import PatientDetails

class SavePatientDetails(forms.ModelForm):
    class Meta:
        model = PatientDetails
        fields = ['cardid', 'age', 'blood','gender', 'phone','address']

#creating patient form
patient_form = SavePatientDetails()

class UploadImage(forms.Form):
    filename = forms.FileField(max_length=200, widget=(forms.FileInput(attrs={'class': 'form-control input-file'})))


class Users_Expert(forms.Form):
    username = forms.CharField(label='username',max_length=500)
    password = forms.CharField(label='password',max_length=500)


