from django.contrib import admin

from .models import Blog, Author, Comment
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'post_date')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'profession')

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Blog, BlogAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Comment, CommentAdmin)