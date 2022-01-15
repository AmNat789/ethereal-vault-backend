import json

from django.apps import apps
from django.http import HttpResponse
from django.shortcuts import render, redirect

from dndPlayerClassBlueprint.models import PlayerClass
from dndPlayerClassBlueprint.forms import PartialPlayerClassForm, CompletePlayerClassForm, ProficienciesForm
from dndPlayerClassBlueprint.utils import get_player_class_blueprints_of_user, TableForm

from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.forms.models import model_to_dict


def index(request):
    if request.method == "GET":
        context = {}
        if request.user.is_authenticated:
            context["player_class_blueprints"] = get_player_class_blueprints_of_user(request)
        return render(request, 'index.html', context)


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


def create_new_player_class(request):
    if request.method == 'POST':
        form = PartialPlayerClassForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            form.save()

        return redirect('index')
    elif request.method == 'GET':
        form = PartialPlayerClassForm()
        context = {'form': form}
        return render(request, 'player-class-blueprint/new-player-class-blueprint.html', context=context)


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


def view_player_class(request, player_class_id):
    blueprint = PlayerClass.objects.get(id=player_class_id)
    if blueprint.user == request.user:
        if request.method == 'POST':
            form = PartialPlayerClassForm(request.POST, instance=blueprint)
            if form.is_valid():
                data = form.save(commit=False)
                data.user = request.user
                form.save()

            return redirect('index')

        if request.method == 'GET':
            context = {}
            context["player_class_id"] = player_class_id
            context["nonForeignParams"] = ["Name", "Description", "Hit die sides"]
            context["form"] = CompletePlayerClassForm(instance=blueprint)
            return render(request, 'player-class-blueprint/view-player-class-blueprint.html', context)
    else:
        return redirect('index')


def delete_player_class(request, player_class_id):
    blueprint = PlayerClass.objects.get(id=player_class_id)
    if blueprint.user == request.user:
        blueprint.delete()
    return redirect('index')


def add_and_update_table(request, player_class_id, table_name):
    blueprint = PlayerClass.objects.get(id=player_class_id)
    if blueprint.user == request.user:
        if request.method == 'POST':
            form = TableForm[table_name[:3].upper()].value(request.POST)
            if form.is_valid():
                form_data = form.save(commit=False)

                blueprint.__dict__[table_name + "_id"] = form_data.id
                form.save()
                blueprint.save()

                return redirect('view-player-class-blueprint', player_class_id)

        if request.method == 'GET':
            table_id = blueprint.__dict__[table_name + "_id"]
            table_model = apps.get_model(app_label='dndPlayerClassBlueprint', model_name=table_name)
            table_instance = table_model.objects.get(id=table_id)

            form = TableForm[table_name[:3].upper()].value(instance=table_instance)
            context = {'form': form, 'table_name': table_name, 'player_class_id': player_class_id}
            return render(request, 'player-class-blueprint/add-and-update.html', context=context)
    else:
        return redirect('view-player-class-blueprint', player_class_id)
