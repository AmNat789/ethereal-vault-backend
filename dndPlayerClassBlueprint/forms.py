from django.forms import ModelForm
from dndPlayerClassBlueprint.models import PlayerClass


class PlayerClassForm(ModelForm):
    class Meta:
        model = PlayerClass
        fields = ["name", "description", "hit_die_sides"]
