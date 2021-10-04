import uuid

from django.contrib.postgres.fields import ArrayField
from django.db import models
from dndPlayerClassBlueprint.choices import Attribute
from dndPlayerClassBlueprint.player_class_models import magic


class Spellcasting(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    spellcasting_attribute = models.CharField(max_length=255, choices=Attribute.get_tuple(), null=True)
    languagesID = models.ForeignKey("magic", on_delete=models.SET_NULL, null=True)
    additional_spells = models.PositiveIntegerField()
    additional_cantrips = models.PositiveIntegerField()
    spell_slots = ArrayField(models.PositiveIntegerField(), size=1)
    spells_prepared = models.PositiveIntegerField(null=True)



    class Meta:
        db_table = "player_class_spellcasting"