from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('user'),
                             on_delete=models.CASCADE)
    body = models.TextField(verbose_name=_('body'), max_length=500)
    slug = models.SlugField(verbose_name=_('slug'), max_length=200)
    photo = models.ImageField(verbose_name=_('photo'), upload_to='images',
                              blank=True)
    location = models.CharField(verbose_name=_('location'), max_length=30, blank=True)
    created_at = models.DateTimeField(verbose_name=_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name=_("updated time"), auto_now=True)
    is_enabled = models.BooleanField(verbose_name=_("is_enabled"), default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'posts'
        verbose_name = _('post')
        verbose_name_plural = _('posts')

    def user_can_like(self, user):
        user_like = user.uvote.all()
        qs = user_like.filter(post=self)
        if qs.exists():
            return True
        return False


class Comment(models.Model):
    post = models.ForeignKey(Post, verbose_name=_('post'), on_delete=models.CASCADE, related_name='post_comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('author'), on_delete=models.CASCADE,
                               related_name='user_comments')
    reply = models.ForeignKey('self', verbose_name=_('reply'), on_delete=models.CASCADE,
                              null=True, blank=True, related_name='rcomment')
    text = models.CharField(verbose_name=_('text'), max_length=100)
    created_at = models.DateTimeField(verbose_name=_('created time'), auto_now_add=True)

    class Meta:
        db_table = 'comments'
        verbose_name = _('comment')
        verbose_name_plural = _('comments')


class LikePost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='post_likes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class LikeComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comment_likes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
