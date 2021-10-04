import uuid

from django.contrib.postgres.fields import ArrayField
from django.db import models

from dndPlayerClassBlueprint.choices import Attribute, Skill


class Proficiencies(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    proficiency_bonus = models.PositiveIntegerField()
    proficient_saving_throws = ArrayField(models.CharField(max_length=255, choices=Attribute.get_tuple(), null=True))
    additional_proficient_saving_throws = models.PositiveIntegerField()
    proficient_skills = ArrayField(models.CharField(max_length=255, choices=Skill.get_tuple()), null=True)
    additional_proficient_skills = models.PositiveIntegerField()
    weapon_proficiencies = ArrayField(models.CharField(max_length=255))

    class Meta:
        db_table = "player_class_proficiencies"
