# Generated by Django 4.0.5 on 2022-06-24 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LikedItem',
        ),
    ]
