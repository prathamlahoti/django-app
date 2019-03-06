from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Post


class PostsListView(ListView):
    """ Displays posts list by specified params """
    model = Post
    template_name = 'posts_list.html'
    context_object_name = 'posts'
    ordering = ['-posted_date']
    paginate_by = 2


class PostDetailView(DetailView):
    """ Displays single post content """
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    """ Allows authorized users to create a new post """
    model = Post
    fields = ['title', 'context']
    template_name = 'post_cud/post_form.html'

    def form_valid(self, form):
        """ Checks form validation for creating posts and  assigns post author to current user"""
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Allows current user to update their post """
    model = Post
    fields = ['title', 'context']
    template_name = 'post_cud/post_form.html'

    def form_valid(self, form):
        """ Checks form validation for updating posts and  assigns post author to current user """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """ Checks, whether current user has permissions to update a post """
        current_post = self.get_object()
        if self.request.user == current_post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Allows current user delete their post """
    model = Post
    success_url = '/'
    template_name = 'post_cud/post_delete_form.html'
    # route to redirect user after successful deleting

    def test_func(self):
        """ Checks, whether current user has permissions to delete a post """
        current_post = self.get_object()
        if self.request.user == current_post.author:
            return True
        return False

