from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, UpdateView
from django.urls import reverse

from .models import Profile

class ProfileDetailView(DetailView):
	model = Profile
	template_name = 'pages/user_profile.html'

	def get_absolute_url(self):
		profile = self.get_object()
		return reverse("user_profile", kwargs={'slug': profile.slug})


class ProfileChangeView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Profile
	fields = [
		'name',
		'surname',
		'bio',
		'image',
	]
	template_name = 'pages/user_profile_change.html'

	def test_func(self):
		obj = self.get_object()
		return obj.user == self.request.user
		