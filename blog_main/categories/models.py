from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=80, verbose_name="Category Title", unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['-title']

    def __str__(self):
        return self.title
