from django.urls import path
from .views import createuser_view

urlpatterns = [
    path("", createuser_view, name="registre_se"),
]