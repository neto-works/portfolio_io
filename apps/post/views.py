from django.shortcuts import render
from .models import Post
import math
from django.core.paginator import Paginator
from apps.categoria.models import Categoria


def blog_view(request):
    p = Post.objects.all()
    categorias = Categoria.objects.all()

    posts = []
    for post in p:
        post_modificado = {
            "titulo": post.titulo,
            "descricao":post.descricao,
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
