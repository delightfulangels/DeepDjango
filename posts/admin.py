from django.contrib import admin
from .models import Post, Comment, Category


class CommentInline(admin.TabularInline):
	model = Comment


class PostAdmin(admin.ModelAdmin):
	list_display = (
		'title', 
		'category', 
		'author', 
		'date'
	)
	inlines = [
		CommentInline,
	]
	prepopulated_fields = {"slug": ("title",)}


class CommentAdmin(admin.ModelAdmin):
	list_display = ('comment', 'author', 'post', 'date')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
