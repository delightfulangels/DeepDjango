from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp

from rest_framework.authtoken.models import TokenProxy

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Profile

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomUser
	list_display = [
		'username',
		'email',
		'is_staff'
	]


class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'name', 'surname', 'bio')
	prepopulated_fields = {'slug': ('user',)}


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)

admin.site.unregister(Group)

admin.site.unregister(SocialToken)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)

admin.site.unregister(TokenProxy)
