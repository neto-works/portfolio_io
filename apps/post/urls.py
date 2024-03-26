from django.urls import path
from .views import blog_view, AHPView

urlpatterns = [
    path("", blog_view, name="blog"),
    path("ahp/", AHPView.as_view(), name="ahp"),
]
