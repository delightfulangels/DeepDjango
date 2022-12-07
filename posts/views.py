from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse

from .forms import CommentForm, PostForm
from .models import Post

class CommentGet(DetailView):
	model = Post
	template_name = 'post/post_detail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['form'] = CommentForm()
		return context


class CommentPost(SingleObjectMixin, FormView):
	model = Post
	form_class = CommentForm
	template_name = 'post/post_detail.html'
	fields = (
		'comment'
	)

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		return super().post(request, *args, **kwargs)

	def form_valid(self, form):
		form.instance.author = self.request.user
		comment = form.save(commit=False)
		comment.post = self.object
		comment.save()
		return super().form_valid(form)
	
	def get_success_url(self):
		post = self.get_object()
		return reverse('post_detail', kwargs={'slug': post.slug})


class PostListView(ListView):
	model = Post
	paginate_by = 12
	ordering = ['-date']
	template_name = 'home.html'


class PostDetailView(DetailView):
	def get(self, request, *args, **kwargs):
		view = CommentGet.as_view()
		return view(request, *args, **kwargs)
	
	def post(self, request, *args, **kwargs):
		view = CommentPost.as_view()
		return view(request, *args, **kwargs)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = (
		'title',
		'body',
	)
	template_name = 'post/post_edit.html'

	def test_func(self):
		obj = self.get_object()
		return obj.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	template_name = 'post/post_delete.html'
	success_url = reverse_lazy('home')

	def test_func(self):
		obj = self.get_object()
		return obj.author == self.request.user


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	template_name = 'post/post_new.html'
	form_class = PostForm

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
