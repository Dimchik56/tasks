# Generated by Django 4.1.4 on 2023-01-20 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='datecreated',
            field=models.DateField(auto_now=True),
        ),
    ]
