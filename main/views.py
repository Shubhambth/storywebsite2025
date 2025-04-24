from django.shortcuts import render
from .models import Post, Category, Tag

def index(request):
    posts = Post.objects.select_related('category').prefetch_related('tags').order_by('-created_at')
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'posts': posts,
        'categories': categories,
        'tags': tags,
    }

    return render(request, 'index.html', context)
