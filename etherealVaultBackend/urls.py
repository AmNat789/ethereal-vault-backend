"""etherealVaultBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from dndPlayerClassBlueprint import views

urlpatterns = [
    path('admin/', admin.site.urls),


    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name="register"),

    path('player-class-blueprint/all', views.player_class__mini_profiles),
    path('player-class-blueprint/<uuid:player_class_id>', views.get_player_class_by_id),
    path('player-class-blueprint/new', views.create_new_player_class, name="create-new-player-class-blueprint"),
    path('player-class-blueprint/delete/<uuid:player_class_id>', views.delete_player_class, name='delete-player-class-blueprint'),
    path('player-class-blueprint/view/<uuid:player_class_id>', views.view_player_class,
         name='view-player-class-blueprint'),

    path('/player-class-blueprint/add-and-update/languages', views.add_and_update_languages)
]
