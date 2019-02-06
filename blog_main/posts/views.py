from django.views.generic import ListView, DetailView
from posts.models import Post


class PostsListView(ListView):
    """ Displays posts list by specified params """
    model = Post
    template_name = 'posts_list.html'
    context_object_name = 'posts'
    ordering = ['-post_posted_date']


class PostDetailView(DetailView):
    """ Displays single post content """
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'