from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    """  """
    post_title = models.CharField(unique=True, max_length=80)
    post_text = models.TextField()
    post_posted_date = models.DateField(default=timezone.now)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __repr__(self):
        return f"""
                   Post ID: {self.pk}, 
                   Post Title: {self.post_tile},
                   Post Author: {self.post_author}
                """

                