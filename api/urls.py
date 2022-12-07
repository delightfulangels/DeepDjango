from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (
	PostAPIView,
	UserAPIView,
)

router = SimpleRouter()
router.register('users', UserAPIView, basename='users')
router.register('', PostAPIView, basename='posts')

urlpatterns = router.urls
