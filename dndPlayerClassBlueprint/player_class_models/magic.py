import uuid

from django.db import models
from django.db.models import JSONField

from dndPlayerClassBlueprint.choices import MagicType, SchoolOfMagic, DamageType


class Magic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    magic_type = models.CharField(max_length=255, choices=MagicType.get_tuple(), null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    school_of_magic = models.CharField(max_length=255, choices=SchoolOfMagic.get_tuple(), null=True)
    damage = models.CharField(max_length=255, null=True)
    healing = models.CharField(max_length=255, null=True)
    damage_type = models.CharField(max_length=255, choices=DamageType.get_tuple(), null=True)
    cast_at_will = models.BooleanField(default=False)
    components = JSONField()
    arcaneFocusReplacesComponents = models.BooleanField(default=False)

    class Meta:
        db_table = "player_class_spellcasting_magic"
