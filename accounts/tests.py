from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):

	def test_create_user(self):
		User = get_user_model()
		user = User.objects.create_user(
			username='test',
			email='test@test.com',
			password='testpass123'
		)
		self.assertEqual(user.username, 'test')
		self.assertEqual(user.email, 'test@test.com')
		self.assertTrue(user.is_active)
		self.assertFalse(user.is_staff)
		self.assertFalse(user.is_superuser)

	def test_create_superuser(self):
		User = get_user_model()
		user = User.objects.create_superuser(
			username='superuser',
			email='superuser@admin.com',
			password='adminadmin'
		)
		self.assertEqual(user.username, 'superuser')
		self.assertEqual(user.email, 'superuser@admin.com')
		self.assertTrue(user.is_active)
		self.assertTrue(user.is_staff)
		self.assertTrue(user.is_superuser)
	