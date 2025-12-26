# blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    # Buscar todos os posts publicados, ordenados pela data mais recente
    posts = Post.objects.filter(publicado=True).order_by('-data_publicacao')
    
    context = {
        'posts': posts,
        'total_posts': posts.count(),
    }
    
    return render(request, 'index.html', context)

def detalhes_post(request, post_id):
    # Buscar o post específico ou retornar 404
    post = get_object_or_404(Post, id=post_id, publicado=True)
    
    context = {
        'post': post,
    }
    
    return render(request, 'post.html', context)