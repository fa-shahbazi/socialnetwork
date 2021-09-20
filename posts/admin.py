from django.contrib import admin

from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'location')


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author')


@admin.register(models.LikePost)
class LikePostAdmin(admin.ModelAdmin):
    list_display = ('post', 'user')


@admin.register(models.LikeComment)
class LikeCommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'user')

