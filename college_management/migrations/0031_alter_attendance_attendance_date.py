# Generated by Django 3.2.9 on 2022-01-20 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_management', '0030_alter_customeuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attendance_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]