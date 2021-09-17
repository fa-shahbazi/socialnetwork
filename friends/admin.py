from django.contrib import admin
from friends.models import Relation
# Register your models here.


@admin.register(Relation)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user')