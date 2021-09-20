from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class Relation(models.Model):
    from_user = models.ForeignKey(User, related_name='followings', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name=_('created time'), auto_now_add=True)

    class Meta:
        db_table = 'relation'
        unique_together = ['from_user', 'to_user']
        verbose_name = _('relation')
        verbose_name_plural = _('relations')

    def __str__(self):
        return f'{self.from_user.username}>{self.to_user.username}'

