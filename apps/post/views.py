from django.shortcuts import render
from .models import Post


def blog_view(request):
    p = Post.objects.all()
    posts = []
    for post in p:
        post_modificado = {
            "titulo": post.titulo,
            "likes": post.likes,
            "imagem": post.imagem.url,
            "blogueiro_id": post.blogueiro_id,
            "categorias": post.categorias.all(),
        }
        posts.append(post_modificado)

    return render(request, "posts/blog.html", context={"posters": posts})
