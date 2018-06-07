from django.contrib.auth.models import Group
from django.contrib import admin

from allauth.account.models import EmailAddress


# ungerister default Django and Allauth app model in admin
admin.site.unregister(Group)
admin.site.unregister(EmailAddress)
