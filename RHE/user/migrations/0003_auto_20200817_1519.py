# Generated by Django 3.1 on 2020-08-17 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200817_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='agreement_document',
            field=models.ImageField(blank=True, null=True, upload_to='agreeement'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='document1',
            field=models.ImageField(blank=True, null=True, upload_to='documents'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='document2',
            field=models.ImageField(blank=True, null=True, upload_to='documents'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='document3',
            field=models.ImageField(blank=True, null=True, upload_to='documents'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic'),
        ),
    ]
