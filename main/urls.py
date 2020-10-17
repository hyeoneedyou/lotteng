from django.urls import path, include
from . import views

urlpatterns = [
    path('team', views.show_team_profile, name = "team"),
]

