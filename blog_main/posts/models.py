from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    """ Post Model """
    post_title = models.CharField(unique=True, max_length=80)
    post_text = models.TextField()
    post_posted_date = models.DateField(default=timezone.now)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __repr__(self):
        return f"""
                   Post ID: {self.pk}, 
                   Post Title: {self.post_title},
                   Post Author: {self.post_author}
                """

    def get_absolute_url(self):
        """ Redirects user to a specific post after post CUD operations """
        return reverse('post-detail', kwargs={'pk': self.pk})
