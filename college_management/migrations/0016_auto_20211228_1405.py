# Generated by Django 3.2.9 on 2021-12-28 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_management', '0015_auto_20211227_1226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_book',
            name='status',
        ),
        migrations.AddField(
            model_name='assign_book',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
