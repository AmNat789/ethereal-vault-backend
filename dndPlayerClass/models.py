import uuid

from django.db import models


class PlayerClass(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    # TODO UserID as FK
    name = models.CharField(max_length=20)
    description = models.TextField()
    hit_die_sides = models.PositiveIntegerField()
    # TODO ProficienciesID
    # TODO LanguagesID
    # TODO FeaturesAndTraitsID
    # TODO SpellcastingID
    # TODO LevellingID

    class Meta:
        db_table = "player_class"
