from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
                                        CreateView, 
                                        UpdateView,
                                        DeleteView
                                        )
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'post-list.html'

# details view
class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = 'post-detail.html'
    
# post crear o createview
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'post-create.html'
    fields = ['title', 'content', 'author']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
# update view
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post-update.html'
    fields = ['title', 'content',]

# delete view
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post-delete.html'
    success_url = reverse_lazy('post-list')  # Redirige a la lista de posts después de eliminar uno
