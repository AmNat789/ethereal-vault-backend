# Generated by Django 3.2.7 on 2021-09-29 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dndPlayerClassBlueprint', '0009_auto_20210929_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='spellcasting',
            name='spellcasting_attribute',
            field=models.CharField(choices=[('STR', 'Strength'), ('DEX', 'Dexterity'), ('CON', 'Constitution'), ('INT', 'Intelligence'), ('WIS', 'Wisdom'), ('CHA', 'Charisma')], max_length=255, null=True),
        ),
    ]
