from django.urls import path
from .views import (
    PostsListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView, PostByCategoryView,
    PostByUserView, PostByTagView,
)

urlpatterns = [
    path('', PostsListView.as_view(), name='posts'),
    path('posts/category/<str:category>/', PostByCategoryView.as_view(), name='posts-category'),
    path('posts/user/<str:username>/', PostByUserView.as_view(), name='posts-user'),
    path('posts/tags/<str:tag>/', PostByTagView.as_view(), name='posts-tag'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/create', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
]
