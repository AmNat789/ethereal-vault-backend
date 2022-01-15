from django import forms
from django.contrib.postgres.fields import ArrayField

from dndPlayerClassBlueprint.models import PlayerClass
from dndPlayerClassBlueprint.player_class_models.proficiencies import Proficiencies
from dndPlayerClassBlueprint import choices


class ArrayWidget(forms.Textarea):
    def format_value(self, value):
        if value is None or len(value) == 0:
            return None
        else:
            return '\n'.join(value.split(','))

    def value_from_datadict(self, data, files, name):
        return data.get(name).splitlines()


class PartialPlayerClassForm(forms.ModelForm):
    class Meta:
        model = PlayerClass
        fields = ["name", "description", "hit_die_sides"]


class CompletePlayerClassForm(forms.ModelForm):
    class Meta:
        model = PlayerClass
        fields = '__all__'


class ProficienciesForm(forms.ModelForm):
    proficient_saving_throws = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                         choices=choices.Attribute.get_tuple())
    proficient_skills = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                  choices=choices.Skill.get_tuple())
    weapon_proficiencies = ArrayField(forms.CharField(max_length=255))

    class Meta:
        model = Proficiencies
        fields = '__all__'
