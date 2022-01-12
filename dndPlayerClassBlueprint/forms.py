from django.forms import ModelForm
from dndPlayerClassBlueprint.models import PlayerClass


class NewPlayerClassForm(ModelForm):
    class Meta:
        model = PlayerClass
        fields = ["name", "description", "hit_die_sides"]


class CompletePlayerClassForm(ModelForm):
    class Meta:
        model = PlayerClass
        fields = '__all__'
