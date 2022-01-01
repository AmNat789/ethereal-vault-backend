import json

from django.http import HttpResponse
from django.shortcuts import render, redirect

from dndPlayerClassBlueprint.models import PlayerClass
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login



def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('index')
    else:
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'registration/register.html', context)


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
