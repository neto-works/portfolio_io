from django.contrib import admin
from django.urls import path, include
from apps.home import urls as home_urls
from apps.post import urls as blog_urls
from apps.blogueiro import urls as blogueiros_urls

urlpatterns = [
    path("", include(home_urls)),
    path("manager/", admin.site.urls, name="manager"),
    path("blog/", include(blog_urls)),
    path("blogueiros/", include(blogueiros_urls)),
    path("contas/",include('django.contrib.auth.urls')),
]
