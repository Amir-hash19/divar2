# Generated by Django 5.1.7 on 2025-03-27 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='age',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
