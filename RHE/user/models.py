from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name =models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_first_name = models.CharField(max_length=100)
    father_middle_name = models.CharField(max_length=100)
    father_last_name = models.CharField(max_length=100)
    email = models.EmailField
    phone_number1 = models.IntegerField
    phone_number2 = models.IntegerField
    date_of_birth = models.DateField
    address_lane1 = models.CharField(max_length=100)
    address_lane2 = models.CharField(max_length=100)
    address_lane3 = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pic',null=True,blank=True)
    bank_name = models.CharField(max_length=100)
    bank_branch = models.CharField(max_length=100)
    pan_number = models.IntegerField
    account_number = models.IntegerField
    ifsc_code = models.CharField(max_length=50)
    micr_code = models.CharField(max_length=50)
    adharcard_number = models.IntegerField
    document1 = models.ImageField(upload_to='documents',null=True,blank=True)
    document2 = models.ImageField(upload_to='documents',null=True,blank=True)
    document3 = models.ImageField(upload_to='documents',null=True,blank=True)
    execution = models.IntegerField
    bd = models.IntegerField
    joining_date = models.DateField
    resignation_date = models.DateField
    agreement_document = models.ImageField(upload_to='agreement',null=True,blank=True)