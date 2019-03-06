from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from categories.models import Category
from tags.models import Tag


class Post(models.Model):
    """ Post Model """
    title = models.CharField(unique=True, max_length=80)
    context = models.TextField()
    posted_date = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    # post meta data
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """ Redirects user to a specific post after post CUD operations """
        return reverse('post-detail', kwargs={'pk': self.pk})
