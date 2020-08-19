# Generated by Django 3.1 on 2020-08-16 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('father_first_name', models.CharField(max_length=100)),
                ('father_middle_name', models.CharField(max_length=100)),
                ('father_last_name', models.CharField(max_length=100)),
                ('address_lane1', models.CharField(max_length=100)),
                ('address_lane2', models.CharField(max_length=100)),
                ('address_lane3', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('profile_picture', models.ImageField(default='default.jpg', upload_to='profile_pic')),
                ('bank_name', models.CharField(max_length=100)),
                ('bank_branch', models.CharField(max_length=100)),
                ('ifsc_code', models.CharField(max_length=50)),
                ('micr_code', models.CharField(max_length=50)),
                ('document1', models.ImageField(upload_to='documents')),
                ('document2', models.ImageField(upload_to='documents')),
                ('document3', models.ImageField(upload_to='documents')),
                ('agreement_document', models.ImageField(upload_to='agreeement')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]