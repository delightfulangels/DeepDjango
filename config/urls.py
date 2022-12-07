from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
	openapi.Info(
		title='DeepDjango API',
		default_version='v1',
		description='Simple API for DeepDjango.com',
		contact=openapi.Contact(email="yosunoro@gmail.com"),
		license=openapi.License(name="BSD License"),
	),
	public=True,
	permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
	# Django admin
    path('admin/', admin.site.urls),
	
	# API
	path('api/', include('api.urls')),
	path('api-auth/', include('rest_framework.urls')),
	path('api/dj-rest-auth/', include('dj_rest_auth.urls')),
	path('api/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

	# API Docs
	path('swagger/', schema_view.with_ui(
		'swagger', cache_timeout=0), name='schema-swagger-ui'),
	path('redoc/', schema_view.with_ui(
		'redoc', cache_timeout=0), name='schema-redoc'),

	# User management
	path('accounts/', include('allauth.urls')),

	# Local apps
	path('profile/', include('accounts.urls')),
	path('pages/', include('pages.urls')),
	path('', include('posts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

