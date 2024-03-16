from django.urls import path
from .views import HomeView, inner_view, portifolio_view

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("portifolio/", portifolio_view, name="portifolio"),
    path("inner/", inner_view, name="inner"),
]
