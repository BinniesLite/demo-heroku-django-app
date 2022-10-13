from django.shortcuts import render
from django.views.generic import ListView, DetailView # new 
from django.views.generic.edit import CreateView, UpdateView, DeleteView # newe
from django.urls import reverse_lazy

from .models import Post 
# Create your views here.

"""
**** Home Page 

**** DetailView: generic class
"""
class BlogListView(ListView):
    model = Post
    template_name: str = 'home.html'
    context_object_name: str = 'all_posts_list'

"""
Detail of each Blog

DetailView: generic class
"""
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    

"""
Update Blog Post

CreateView: generic class
"""
class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'


class BlogUpdateView(UpdateView): #new
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView): #new
    model = Post
    template_name = 'post_delete.html'
    success_url: str = reverse_lazy('home')




