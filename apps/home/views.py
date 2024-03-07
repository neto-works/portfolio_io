from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login


def inner_view(request):
    return render(request,'home/inner-page.html')

def portifolio_view(request):
    return render(request,'home/portfolio-details.html')

class HomeView(View):
    def get(self, request):
        return render(request,'home/home.html')
