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
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=_('likes'),
                                   related_name="liker", blank=True, symmetrical=False)
    created_at = models.DateTimeField(verbose_name=_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name=_("updated time"), auto_now=True)
    is_enabled = models.BooleanField(verbose_name=_("is_enabled"), default=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'posts'
        verbose_name = _('post')
        verbose_name_plural = _('posts')

    def number_of_likes(self):
        if self.likes.count():
            return self.likes.count()
        else:
            return 0

    def likes_count(self):
        return self.pvote.count()

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
    is_reply = models.BooleanField(verbose_name=_('is_reply'), default=False)
    text = models.CharField(verbose_name=_('text'), max_length=100)
    created_at = models.DateTimeField(verbose_name=_('created time'), auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'comments'
        verbose_name = _('comment')
        verbose_name_plural = _('comments')


class Vote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='pvote')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, related_name='uvote')

    def __str__(self):
        return f'{self.user} liked {self.post}'

