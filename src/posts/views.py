from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from . import models


class PostListView(ListView):
    model = models.Post
    template_name = 'posts/list.html'
    ordering = 'created'


class PostDetailView(DetailView):
    model = models.Post
    template_name = 'posts/detail.html'


class PostCreateView(CreateView):
    model = models.Post
    template_name = 'posts/create.html'
    fields = '__all__'


class PostUpdateView(UpdateView):
    model = models.Post
    template_name = 'posts/update.html'
    fields = ['message', 'title']
