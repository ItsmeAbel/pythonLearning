from pathlib import Path
from django.urls import path
from . import views

#url configuration
urlpatterns = [
    path("hello/", views.hell_world) #always end path with /
]