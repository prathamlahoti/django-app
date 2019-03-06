from django.shortcuts import render
from django.views.generic import ListView
from .models import Category


class CategoryListView(ListView):
    """ List of all available categories """
    model = Category
    context_object_name = 'categories'
    ordering = ['-title']



