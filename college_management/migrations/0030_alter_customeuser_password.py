# Generated by Django 3.2.9 on 2022-01-20 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_management', '0029_alter_attendance_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeuser',
            name='password',
            field=models.CharField(max_length=16666),
        ),
    ]