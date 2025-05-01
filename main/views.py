from django.shortcuts import render ,  get_object_or_404
from .models import Post, Category, Tag
from django.db.models import Q

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


def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category).order_by('-views')

    return render(request, 'category_posts.html', {
        'category': category,
        'posts': posts
    })




def search_posts(request):
    query = request.GET.get('q')
    posts = []

    if query:
        posts = Post.objects.filter(Q(title__icontains=query)).order_by('-id')

    return render(request, 'search_results.html', {
        'query': query,
        'posts': posts,
    })

def contact(request):
    return render(request,"contact.html")

