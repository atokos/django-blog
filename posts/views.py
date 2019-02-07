from django.shortcuts import redirect, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

from . import forms
from . import models


class PostListView(ListView):
    model = models.Post
    template_name = 'posts/list.html'
    ordering = 'created'


class PostDetailView(FormMixin, DetailView):
    model = models.Post
    template_name = 'posts/detail.html'
    form_class = forms.CommentForm

    def get_success_url(self):
        return reverse('posts-detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['comments'] = self.object.comment_set.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        new_comment = form.save(commit=False)
        new_comment.post = self.get_object()
        new_comment.save()
        return super(PostDetailView, self).form_valid(form)


class PostCreateView(LoginRequiredMixin, CreateView):
    # CreateView
    model = models.Post
    template_name = 'posts/create.html'
    fields = '__all__'

    # LoginRequiredMixin
    login_url = 'login'
    permission_denied_message = 'Log in to create a new post'


class PostUpdateView(PermissionRequiredMixin, UpdateView):
    # UpdateView
    model = models.Post
    template_name = 'posts/update.html'
    fields = ['message', 'title']

    # PermissionRequiredMixin
    login_url = 'login'
    permission_denied_message = 'You can only edit your own posts'
    permission_required = 'posts.change_post'
