from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db import models

from PIL import Image

class CustomUser(AbstractUser):
	pass


class Profile(models.Model):
	user = models.OneToOneField(CustomUser, unique=True, on_delete=models.CASCADE)
	name = models.CharField(null=True, blank=True, default='Нет информации', max_length=255, verbose_name='Имя')
	surname = models.CharField(null=True, blank=True, default='Нет информации', max_length=255, verbose_name='Фамилия')
	bio = models.CharField(null=True, blank=True, default='Нет информации', max_length=400, verbose_name='О себе')
	image = models.ImageField(null=True, blank=True, default='default.jpg', upload_to='profile_pics', verbose_name='Аватар')
	slug = models.SlugField(null=False, blank=False, verbose_name='URL')

	class Meta:
		verbose_name = 'Профиль'
		verbose_name_plural = 'Профили'

	def __str__(self):
		return f'{self.user.username} профиль'

	def get_absolute_url(self):
		return reverse("user_profile", kwargs={"slug": self.slug})

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.user)

		super().save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)
