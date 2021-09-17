from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Profile(models.Model):
    CHOICES = (
        ("female", "f"),
        ("male", "m"),
        ("others", "other")
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                verbose_name=_('user'), on_delete=models.CASCADE)
    location = models.CharField(max_length=140)
    gender = models.CharField(max_length=140, choices=CHOICES)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='avatars')
    bio = models.TextField(_('bio'), blank=True)
    age = models.PositiveSmallIntegerField(_('age'))
    phone_number = models.PositiveBigIntegerField(_('phone number'), unique=True)
    created_at = models.DateTimeField(verbose_name=_('created time'), auto_now_add=True)


    class Meta:
        db_table = 'profiles'
        verbose_name = _('profiles')
        verbose_name_plural = _('profiles')


def save_profile(sender, **kwargs):
    if kwargs['created']:
        p1 = Profile(user=kwargs['instance'])
        p1.save()


post_save.connect(save_profile, sender=User)