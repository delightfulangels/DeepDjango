from django.urls import path

from .views import (
	PostListView,
	PostDetailView,
	PostUpdateView,
	PostDeleteView,
	PostCreateView,
)

urlpatterns = [
	# Post's CRUD
	path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
	path('post/<slug:slug>/edit/', PostUpdateView.as_view(), name='post_edit'),
	path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
	path('new/', PostCreateView.as_view(), name='post_new'),

	# Homepage
	path('', PostListView.as_view(), name='home'),
]
