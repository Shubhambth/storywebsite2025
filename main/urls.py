from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('post/<slug:slug>/', views.detailpost, name='detailpost'),
    path('category/<slug:slug>/', views.category_posts, name='category_posts'),
    path('search/', views.search_posts, name='search_posts'),
]