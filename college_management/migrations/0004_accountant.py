# Generated by Django 3.2.9 on 2021-12-03 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college_management', '0003_department_faculty_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accountant',
            fields=[
                ('customeuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='college_management.customeuser')),
                ('Qualification', models.CharField(max_length=20)),
                ('Salary', models.CharField(max_length=10)),
                ('created_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('college_management.customeuser',),
        ),
    ]
