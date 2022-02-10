# Generated by Django 3.2.9 on 2022-01-06 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college_management', '0018_marks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department', to='college_management.department'),
        ),
    ]
