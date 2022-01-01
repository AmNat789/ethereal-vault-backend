import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from dndPlayerClassBlueprint.models import PlayerClass
from dndPlayerClassBlueprint.player_class_models import proficiencies
from dndPlayerClassBlueprint.player_class_models.proficiencies import Proficiencies
from django.core import serializers

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


def get_player_class_by_id(request, player_class_id):
    if request.method == 'GET':
        try:
            selected_player_class = PlayerClass.objects.filter(id=player_class_id)
            response = serializers.serialize("json", selected_player_class)
        except:
            response = json.dumps({"Error": "Something went wrong"})
        return HttpResponse(response, content_type='text/json')


def create_new_player_class(request):
    print(request.method)
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            return HttpResponse(data, content_type='text/json')
        except Exception as e:
            print(e)