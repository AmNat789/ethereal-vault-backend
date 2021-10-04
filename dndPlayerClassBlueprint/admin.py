from django.contrib import admin
from .models import PlayerClass
from .player_class_models.magic import Magic
from .player_class_models.spellcasting import Spellcasting

admin.site.register(PlayerClass)
admin.site.register(Magic)
admin.site.register(Spellcasting)
