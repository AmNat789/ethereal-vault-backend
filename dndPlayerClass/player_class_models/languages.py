import uuid

from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import PositiveIntegerField


class Languages(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    given_languages = ArrayField(models.CharField(max_length=30), blank=True)
    additional_languages = PositiveIntegerField()

    class Meta:
        db_table = "player_class_languages"
