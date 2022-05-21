from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class BlogappListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'
    
class BlogappDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'