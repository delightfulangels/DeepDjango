from django.db import models
from django.conf import settings
from django.urls import reverse

from ckeditor.fields import RichTextField
from pytils.translit import slugify

class Post(models.Model):
	title = models.CharField(max_length=255, verbose_name='Название')
	body = RichTextField(blank=True, null=True, verbose_name="Текст публикации")
	date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
	author = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		verbose_name='Автор'
	)
	category = models.CharField(max_length=255, default='None', verbose_name="Категория", blank=True)
	image = models.ImageField(upload_to='posts/', blank=True, verbose_name="Изображение")
	slug = models.SlugField(null=False, unique=True)

	class Meta:
		verbose_name = 'Публикация'
		verbose_name_plural = 'Публикации'

	def __str__(self):
		return self.title[:50]

	def get_absolute_url(self):
		return reverse("post_detail", kwargs={"slug": self.slug})

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		return super().save(*args, **kwargs)
	

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	comment = models.CharField(max_length=140, verbose_name="Текст комментария")
	author = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		verbose_name='Автор комментария'
	)
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'

	def __str__(self):
		return self.comment[:50]

	def get_absolute_url(self):
		return reverse("home")


class Category(models.Model):
	name = models.CharField(max_length=50, unique=True, verbose_name='Название')

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	def __str__(self):
		return self.name[:50]
	
	def get_absolute_url(self):
		return reverse('home')
	