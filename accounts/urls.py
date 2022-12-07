from django.urls import path

from .views import ProfileDetailView, ProfileChangeView

urlpatterns = [
	# Profile URL's
	path('<slug:slug>', ProfileDetailView.as_view(), name='user_profile'),
	path('<slug:slug>/update', ProfileChangeView.as_view(), name='user_profile_change'),
]