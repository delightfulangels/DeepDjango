from django.views.generic import TemplateView, ListView
from posts.models import Post
from django.db.models import Q

class OtherCategoryListView(ListView):
	model = Post
	ordering = ['-date']
	paginate_by = 5
	context_object_name = 'post_list'
	template_name = 'categories/category_other.html'

	def get_queryset(self):
		return Post.objects.filter(
			Q(category__icontains='Другое')
		)


class DjangoRestCategoryListView(ListView):
	model = Post
	ordering = ['-date']
	paginate_by = 5
	context_object_name = 'post_list'
	template_name = 'categories/category_django_rest.html'

	def get_queryset(self):
		return Post.objects.filter(
			Q(category__icontains='Django REST')
		)


class DjangoCategoryListView(ListView):
	model = Post
	ordering = ['-date']
	paginate_by = 5
	context_object_name = 'post_list'
	template_name = 'categories/category_django.html'

	def get_queryset(self):
		return Post.objects.filter(
			Q(category__icontains='Django')
		)


class PythonCategoryListView(ListView):
	model = Post
	ordering = ['-date']
	paginate_by = 5
	context_object_name = 'post_list'
	template_name = 'categories/category_python.html'

	def get_queryset(self):
		return Post.objects.filter(
			Q(category__icontains='Python')
		)


class SearchResultsListView(ListView):
	model = Post
	ordering = ['-date']
	context_object_name = 'post_list'
	template_name = 'pages/search_results.html'
	
	def get_queryset(self):
		query = self.request.GET.get('q', None)
		if query:
			return Post.objects.filter(
				Q(title__icontains=query) | Q(body__icontains=query)
			)
		else:
			return []


class AboutPageView(TemplateView):
	template_name = 'pages/about.html'
