from django.contrib import admin

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
