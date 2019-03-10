from .models import Category


def add_variable_to_context(request):
	return {
		# Getting first 6 categories
		"categories": Category.objects.all()[:6]
	}