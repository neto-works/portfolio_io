from django.shortcuts import render
from .models import Post


def blog_view(request):
    posters = Post.objects.all()

    context = {"posters": posters}
    return render(request, "posts/blog.html", context)
