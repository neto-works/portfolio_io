from django.urls import path
from .views import blog_view, AHPView, search

urlpatterns = [
    path("", blog_view, name="blog"),
    path("ahp/", AHPView.as_view(), name="ahp"),
    path("search/", search, name="search"),
]
