import math
from django.shortcuts import render
from django.views import View
from .models import Post
from django.core.paginator import Paginator
from apps.categoria.models import Categoria
# from .utils.meu import AHP
# from matplotlib import pyplot as plt
# from .forms import AHPfForm


def blog_view(request):
    p = Post.objects.all()
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

class AHPView(View):

    def get(self, request):
        # form = AHPfForm()
        # context = {"form_contato": form}
        return render(request, "posts/ahp.html")

    # def post(self, request):
    #     exemplo = AHP(metodo='',precisao=3,alternativas=['Tom', 'Dick', 'Harry'],
    #     criterios=['Experiência', 'Educação', 'Carisma', 'Idade'],subcriterios={},
    #     matrizes_de_preferencias={
    #         'Experiência': [
    #             [1, 1 / 4, 4],
    #             [4, 1, 9],
    #             [1 / 4, 1 / 9, 1]
    #         ],
    #         'Educação': [
    #             [1, 3, 1 / 5],
    #             [1 / 3, 1, 1 / 7],
    #             [5, 7, 1]
    #         ],
    #         'Carisma': [
    #             [1, 5, 9],
    #             [1 / 5, 1, 4],
    #             [1 / 9, 1 / 4, 1]
    #         ],
    #         'Idade': [
    #             [1, 1 / 3, 5],
    #             [3, 1, 9],
    #             [1 / 5, 1 / 9, 1]
    #         ],
    #         'criterios': [
    #             [1, 4, 3, 7],
    #             [1 / 4, 1, 1 / 3, 3],
    #             [1 / 3, 3, 1, 5],
    #             [1 / 7, 1 / 3, 1 / 5, 1]
    #         ]
    #     },log=True)

    #     resultado = exemplo.resultado()
    #     print(resultado)

    #     plt.bar(resultado.keys(), resultado.values())
    #     plt.ylabel('Prioridade')
    #     plt.savefig('meu_grafico.png')

    #     form = AHPfForm(request.POST or None)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("home")
    #     else:
    #         context = {"form_contato": form}
    #         return render(request, "posts/ahp.html", context)

