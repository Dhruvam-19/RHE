from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.files.uploadedfile import SimpleUploadedFile

class Userregisterform(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class Profile_form(forms.Form):
    profile_picture = forms.ImageField()
    first_name =forms.CharField()
    middle_name = forms.CharField()
    last_name = forms.CharField()
    father_first_name = forms.CharField()
    father_middle_name = forms.CharField()
    father_last_name = forms.CharField()
    email = forms.EmailField()
    phone_number1 = forms.IntegerField()
    phone_number2 = forms.IntegerField()
    date_of_birth = forms.DateField()
    address_lane1 = forms.CharField()
    address_lane2 = forms.CharField()
    address_lane3 = forms.CharField()
    state = forms.CharField()
    country = forms.CharField()
    bank_name = forms.CharField()
    bank_branch = forms.CharField()
    pan_number = forms.IntegerField()
    account_number = forms.IntegerField()
    ifsc_code = forms.CharField()
    micr_code = forms.CharField()
    adharcard_number = forms.IntegerField()
    execution = forms.IntegerField()
    bd = forms.IntegerField()
    joining_date = forms.DateField()
    resignation_date = forms.DateField()
    agreement_document = forms.ImageField()
    document1 = forms.ImageField()
    document2 = forms.ImageField()
    document3 = forms.ImageField()