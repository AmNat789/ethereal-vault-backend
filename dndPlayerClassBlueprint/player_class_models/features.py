import uuid

from django.db import models


class Features(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    description = models.TextField()

    class Meta:
        db_table = "player_class_features"
