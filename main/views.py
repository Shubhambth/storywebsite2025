from django.shortcuts import render ,  get_object_or_404
from .models import Post, Category, Tag

def index(request):
    posts = Post.objects.select_related('category').prefetch_related('tags').order_by('-created_at')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    popular_posts = Post.objects.order_by('-views')[:5]

    context = {
        'posts': posts,
        'categories': categories,
        'tags': tags,
        'popular_posts': popular_posts
    }

    return render(request, 'index.html', context)


def detailpost(request,slug):
    post = get_object_or_404(Post,slug=slug)
    post.views += 1
    post.save(update_fields=['views'])
    related_posts = Post.objects.filter(category=post.category).exclude(id=post.id)[:3]
    
    return render(request,'detailpage.html',{'post':post,'related_posts': related_posts})
