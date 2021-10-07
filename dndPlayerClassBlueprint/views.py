import json

from django.http import HttpResponse

from dndPlayerClassBlueprint.models import PlayerClass


def player_class__mini_profiles(request):
    if request.method == 'GET':
        try:
            player_classes = PlayerClass.objects.all()
            data = dict({})
            for player_class in player_classes:
                data[str(player_class.id)] = {"class_name": player_class.name,
                                              "class_description": player_class.description}
            response = json.dumps({"player_class__mini_profiles": data})
        except:
            response = json.dumps({"Error": "Something went wrong"})

        return HttpResponse(response, content_type='text/json')
