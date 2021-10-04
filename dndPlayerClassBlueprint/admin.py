from django.contrib import admin
from .models import PlayerClass
from .player_class_models.magic import Magic

admin.site.register(PlayerClass)
admin.site.register(Magic)
