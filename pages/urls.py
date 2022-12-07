from django.urls import path

from .views import (
	AboutPageView,
	DjangoCategoryListView,
	DjangoRestCategoryListView, 
	PythonCategoryListView,
	SearchResultsListView, 
	OtherCategoryListView,
)

urlpatterns = [
	# User navigation
	path('about/', AboutPageView.as_view(), name='about'),
	path('search/', SearchResultsListView.as_view(), name='search_results'),

	# Search by category
	path('python/', PythonCategoryListView.as_view(), name='python'),
	path('django/', DjangoCategoryListView.as_view(), name='django'),
	path('django-rest/', DjangoRestCategoryListView.as_view(), name='django-rest'),
	path('other/', OtherCategoryListView.as_view(), name='other'),
]
