# Generated by Django 3.2.9 on 2021-12-28 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_management', '0016_auto_20211228_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assign_book',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]