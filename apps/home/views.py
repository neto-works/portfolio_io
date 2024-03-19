from django.shortcuts import render, redirect
from django.views import View
from .forms import ContatoForm
from .models import Contato
from apps.projeto.models import Projeto


class HomeView(View):

    def get(self, request):
        form = ContatoForm()
        projetos = Projeto.objects.all()

        context = {"form_contato": form, "projetos": projetos}
        return render(request, "home/home.html", context)

    def post(self, request):
        form = ContatoForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            context = {"form_contato": form}
            return render(request, "home/home.html", context)


def inner_view(request):
    return render(request, "home/inner-page.html")


def portifolio_view(request):
    return render(request, "home/portfolio-details.html")
