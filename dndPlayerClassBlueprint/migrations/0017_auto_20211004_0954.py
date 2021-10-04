# Generated by Django 3.2.7 on 2021-10-04 07:54

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dndPlayerClassBlueprint', '0016_alter_spellcasting_spell_slots'),
    ]

    operations = [
        migrations.AddField(
            model_name='magic',
            name='damage_type',
            field=models.CharField(choices=[('ACID', 'Acid'), ('BLUDGEONING', 'Bludgeoning'), ('COLD', 'Cold'), ('FIRE', 'Fire'), ('FORCE', 'Force'), ('LIGHTNING', 'Lightning'), ('NECROTIC', 'Necrotic'), ('PIERCING', 'Piercing'), ('POISON', 'Poison'), ('RADIANT', 'Radiant'), ('SLASHING', 'Slashing'), ('THUNDER', 'Thunder')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='magic',
            name='magic_type',
            field=models.CharField(choices=[('SPELL', 'Spell'), ('CANTRIP', 'Cantrip')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='magic',
            name='school_of_magic',
            field=models.CharField(choices=[('CONJURATION', 'Conjuration'), ('NECROMANCY', 'Necromancy'), ('EVOCATION', 'Evocation'), ('ABJURATION', 'Abjuration'), ('TRANSMUTATION', 'Transmutation'), ('DIVINATION', 'Divination'), ('ENCHANTMENT', 'Enchantment'), ('ILLUSION', 'Illusion')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='spellcasting',
            name='spell_slots',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), size=1),
        ),
    ]