import math
from django.shortcuts import render
from django.views import View
from .models import Post
from django.core.paginator import Paginator
from apps.categoria.models import Categoria
from .utils.meu import AHP


def blog_view(request):
    p = Post.objects.all().order_by("-created_at")
    categorias = Categoria.objects.all()

    posts = []
    for post in p:
        post_modificado = {
            "titulo": post.titulo,
            "descricao": post.descricao,
            "likes": post.likes,
            "imagem": post.imagem.url,
            "blogueiro_id": post.blogueiro_id,
            "created_at": post.created_at,
            "categorias": post.categorias.all(),
        }
        posts.append(post_modificado)

    try:
        pagina_atual = int(request.GET.get("page", 1))
    except ValueError:
        pagina_atual = 1

    paginator = Paginator(posts, 10)
    posts_paginados = paginator.get_page(pagina_atual)

    pagination_range = make_pagination_range(paginator.page_range, 10, pagina_atual)

    return render(
        request,
        "posts/blog.html",
        context={
            "posts_paginados": posts_paginados,
            "links_pages": pagination_range,
            "categorias": categorias,
        },
    )


def make_pagination_range(page_range, links_mostrados, qual_pagina_esta):
    metade_range = math.ceil(links_mostrados / 2)
    start_range = qual_pagina_esta - metade_range
    stop_range = qual_pagina_esta + metade_range
    total_page = len(page_range)
    start_range_offset = abs(start_range) if start_range < 0 else 0

    if start_range < 0:
        start_range = 0
        stop_range += start_range_offset

    if stop_range >= total_page:
        start_range = start_range - abs(total_page - stop_range)

    pagination = page_range[start_range:stop_range]

    return {
        "pagination": pagination,
        "page_range": page_range,
        "quantidade_paginas": 10,
        "current_page": qual_pagina_esta,
        "total_pages": total_page,
        "start_range": start_range,
        "stop_range": stop_range,
        "primeira_pagina_na_telah": qual_pagina_esta > metade_range,
        "ultima_pagina_na_telah": stop_range < total_page,
    }


def pegar_numero(request, nome_campo) -> float:
    numero_string = request.POST.get(nome_campo)
    if "/" in numero_string:
        partes = numero_string.split("/")
        return float(partes[0]) / float(partes[1])
    return float(numero_string) if numero_string is not None and (numero_string !='') else 0.0

class AHPView(View):

    def get(self, request):
        return render(request, "posts/ahp.html")

    def post(self, request):
        exemplo = AHP(
            metodo="",
            precisao=3,
            alternativas=["Fiat Uno 2011", "Fiat Argo 2022", "NISSAN Kicks 2024"],
            criterios=[
                "Preço popular",
                "Econômia",
                "Capacidade pessoas",
                "Tecnologia embarcada",
            ],
            subcriterios={},
            matrizes_de_preferencias={
                "Preço popular": [
                    [
                        1,
                        pegar_numero(request, "preco01"),
                        pegar_numero(request, "preco02"),
                    ],
                    [
                        pegar_numero(request, "preco10"),
                        1,
                        pegar_numero(request, "preco12"),
                    ],
                    [
                        pegar_numero(request, "preco20"),
                        pegar_numero(request, "preco21"),
                        1,
                    ],
                ],
                "Econômia": [
                    [
                        1,
                        pegar_numero(request, "economia01"),
                        pegar_numero(request, "economia02"),
                    ],
                    [
                        pegar_numero(request, "economia10"),
                        1,
                        pegar_numero(request, "economia12"),
                    ],
                    [
                        pegar_numero(request, "economia20"),
                        pegar_numero(request, "economia21"),
                        1,
                    ],
                ],
                "Capacidade pessoas": [
                    [
                        1,
                        pegar_numero(request, "capacidade01"),
                        pegar_numero(request, "capacidade02"),
                    ],
                    [
                        pegar_numero(request, "capacidade10"),
                        1,
                        pegar_numero(request, "capacidade12"),
                    ],
                    [
                        pegar_numero(request, "capacidade20"),
                        pegar_numero(request, "capacidade21"),
                        1,
                    ],
                ],
                "Tecnologia embarcada": [
                    [
                        1,
                        pegar_numero(request, "tecnologia01"),
                        pegar_numero(request, "tecnologia02"),
                    ],
                    [
                        pegar_numero(request, "tecnologia10"),
                        1,
                        pegar_numero(request, "tecnologia12"),
                    ],
                    [
                        pegar_numero(request, "tecnologia20"),
                        pegar_numero(request, "tecnologia21"),
                        1,
                    ],
                ],
                "criterios": [
                    [
                        1,
                        pegar_numero(request, "pesoglobal01"),
                        pegar_numero(request, "pesoglobal02"),
                        pegar_numero(request, "pesoglobal03"),
                    ],
                    [
                        pegar_numero(request, "pesoglobal10"),
                        1,
                        pegar_numero(request, "pesoglobal12"),
                        pegar_numero(request, "pesoglobal13"),
                    ],
                    [
                        pegar_numero(request, "pesoglobal20"),
                        pegar_numero(request, "pesoglobal21"),
                        1,
                        pegar_numero(request, "pesoglobal23"),
                    ],
                    [
                        pegar_numero(request, "pesoglobal30"),
                        pegar_numero(request, "pesoglobal31"),
                        pegar_numero(request, "pesoglobal32"),
                        1,
                    ],
                ],
            },
            log=True,
        )
        resultado = exemplo.resultado()
        context = {"resultado": resultado}
        if resultado:
            return render(request, "posts/ahp.html", context)
        else:
            context = {"resultado": "Algo de errado não esta certo!"}
            return render(request, "posts/ahp.html", context)
