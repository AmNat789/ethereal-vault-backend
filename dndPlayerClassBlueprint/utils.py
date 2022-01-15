from dndPlayerClassBlueprint.models import PlayerClass
from dndPlayerClassBlueprint.forms import *
from enum import Enum


def get_player_class_blueprints_of_user(request) -> list:
    if request.method == "GET":
        return PlayerClass.objects.filter(user_id=request.user)


class TableForm(Enum):
    PRO = ProficienciesForm
