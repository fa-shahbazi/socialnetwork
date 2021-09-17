from django.contrib import admin
from .models import Post, Comment, Vote
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug')
    list_filter = ('slug',)
    search_fields = ('user', 'location')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'reply')


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('user',)


