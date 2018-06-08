from django.contrib.auth.models import Group
from django.contrib import admin

from allauth.account.models import EmailAddress

from .models import User, Advertiser


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username',
                    'role', 'team',
                    'last_login', 'date_joined')


@admin.register(Advertiser)
class AdvertiserAdmin(admin.ModelAdmin):
    list_display = ('email', 'team',
                    'manager', 'publisher',
                    'date_joined')


# ungerister default Django and Allauth app model in admin
admin.site.unregister(Group)
admin.site.unregister(EmailAddress)