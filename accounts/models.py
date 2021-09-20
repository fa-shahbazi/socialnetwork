from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    CHOICES = (
        ("female", "f"),
        ("male", "m"),
        ("others", "other")
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                verbose_name=_('user'), on_delete=models.CASCADE)
    location = models.CharField(max_length=140, blank=True)
    gender = models.CharField(max_length=140, choices=CHOICES)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='avatars', null=True)
    bio = models.TextField(_('bio'), blank=True)
    age = models.PositiveSmallIntegerField(_('age'), blank=True, null=True)
    phone_number = models.PositiveBigIntegerField(_('phone number'), unique=True,
                                                  blank=True, null=True)
    created_at = models.DateTimeField(verbose_name=_('created time'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('updated at'), auto_now=True)

    class Meta:
        db_table = 'profiles'
        verbose_name = _('profiles')
        verbose_name_plural = _('profiles')

    def get_user_id(self):
        return self.user.id

    def get_username(self):
        return self.user.username

    def __str__(self):
        return str(self.user)
