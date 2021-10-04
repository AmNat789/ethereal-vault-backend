import json

from django.http import HttpResponse

from dndPlayerClassBlueprint.models import PlayerClass


def get_all_mini_player_classes(request):
    response = json.dumps({"Error": "something went wrong"})
    if request.method == 'GET':
        try:
            classes = PlayerClass.objects.all()
            data = dict({})
            for player_class in classes:
                data[str(player_class.id)] = {"Name": player_class.name,
                                              "Description": player_class.description}
            response = json.dumps({"all_player_classes": data})
        except:
            response = json.dumps({"Error": "Something went wrong"})

    return HttpResponse(response, content_type='text/json')
