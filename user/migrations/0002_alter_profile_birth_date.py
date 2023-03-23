# Generated by Django 4.1.7 on 2023-03-23 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="birth_date",
            field=models.DateField(
                help_text="The age will be populated after you save your date of birth_date. It can't be edited"
            ),
        ),
    ]
