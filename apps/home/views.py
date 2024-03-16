from django.shortcuts import render, redirect
from django.views import View
from .forms import ContatoForm
from .models import Contato


class HomeView(View):

    def get(self, request):
        form = ContatoForm()
        context = {"form_contato": form}
        return render(request, "home/home.html", context)

    def post(self, request):
        form = ContatoForm(request.POST or None)  # Instancia o formulário com os dados submetidos
        if (
            form.is_valid()
        ):  # Verifica se o formulário é válido, se é valido tem coisa dentro
            form.save()  # Salva os dados no banco de dados
            return redirect(
                "home"
            )  # Redireciona para a página desejada após o envio do formulário
        else:
            # Se o formulário não for válido, renderiza o template novamente com os erros
            context = {"form_contato": form}
            return render(request, "home/home.html", context)


def inner_view(request):
    return render(request, "home/inner-page.html")


def portifolio_view(request):
    return render(request, "home/portfolio-details.html")
