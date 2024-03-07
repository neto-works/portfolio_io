from django.shortcuts import render

# Create your views here.
def blogueiros_views(request):
    return render(request,'blogueiros/index.html')
