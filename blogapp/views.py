#from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
    )
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
class BlogappListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'
    
class BlogappDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    
class BlogappCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ['title', 'author', 'body']
    
class BlogappUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ['title', 'body']
    
class BlogappDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blogapphome')