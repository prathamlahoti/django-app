from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=40, verbose_name="Tag Name", unique=True)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        ordering = ['-title']

    def __str__(self):
        return self.title
