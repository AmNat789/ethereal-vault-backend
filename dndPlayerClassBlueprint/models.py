import uuid

from django.db import models
from dndPlayerClassBlueprint.player_class_models import languages, features, spellcasting, proficiencies


class PlayerClass(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    name = models.CharField(max_length=20)
    description = models.TextField()
    hit_die_sides = models.PositiveIntegerField()
    proficienciesID = models.ForeignKey("proficiencies", on_delete=models.SET_NULL, null=True)
    languagesID = models.ForeignKey("languages", on_delete=models.SET_NULL, null=True)
    features = models.ManyToManyField('features', null=True, name='features_junction')
    spellcastingID = models.ForeignKey("spellcasting", on_delete=models.SET_NULL, null=True)
    # TODO LevellingID

    class Meta:
        db_table = "player_class"
