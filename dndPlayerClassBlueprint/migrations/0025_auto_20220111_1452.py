# Generated by Django 3.2.7 on 2022-01-11 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dndPlayerClassBlueprint', '0024_playerclass_userid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playerclass',
            old_name='languagesID',
            new_name='languages',
        ),
        migrations.RenameField(
            model_name='playerclass',
            old_name='proficienciesID',
            new_name='proficiencies',
        ),
        migrations.RenameField(
            model_name='playerclass',
            old_name='spellcastingID',
            new_name='spellcasting',
        ),
        migrations.RenameField(
            model_name='playerclass',
            old_name='userID',
            new_name='user',
        ),
    ]
