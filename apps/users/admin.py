from django.contrib.auth.models import Group
from django.contrib import admin

from allauth.account.models import EmailAddress

from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


# unregister default Django and All Auth app model in admin
admin.site.unregister(Group)
admin.site.unregister(EmailAddress)
