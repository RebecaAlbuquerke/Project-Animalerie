# Generated by Django 3.2.9 on 2021-11-28 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animalerie', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='nom_animal',
            new_name='id_animal',
        ),
        migrations.RenameField(
            model_name='equipement',
            old_name='nom_equipement',
            new_name='id_equip',
        ),
    ]