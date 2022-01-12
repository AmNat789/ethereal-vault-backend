from dndPlayerClassBlueprint.models import PlayerClass


def get_player_class_blueprints_of_user(request) -> list:
    if request.method == "GET":
        return PlayerClass.objects.filter(user_id=request.user)