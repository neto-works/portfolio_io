from django.urls import path
from .views import blogueiros_views

urlpatterns = [
    path("", blogueiros_views, name="blogueiros"),
]
