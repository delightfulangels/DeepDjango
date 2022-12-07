from dataclasses import fields
from django import forms

from .models import Category, Comment, Post

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
	choice_list.append(item)


class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'category', 'body', 'image')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'})
		}


class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ('comment',)
