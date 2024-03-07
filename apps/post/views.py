from django.shortcuts import render


def blog_view(request):
    return render(request,'posts/blog.html')
