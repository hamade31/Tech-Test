# Generated by Django 3.0.3 on 2021-03-13 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacherdirectory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherprofile',
            name='room_number',
            field=models.IntegerField(help_text='Class room number', unique=True),
        ),
    ]
