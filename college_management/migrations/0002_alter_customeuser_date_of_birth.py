# Generated by Django 3.2.9 on 2021-12-02 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeuser',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]