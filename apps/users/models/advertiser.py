from django.db import models
from django.utils.translation import ugettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

from core.utils import uuid_hex
from core.validators import validate_pdf_ext


class Advertiser(models.Model):
    username = models.CharField(max_length=32, default=uuid_hex(),
                                blank=False, unique=True)
    email = models.EmailField(_('email'), max_length=254, unique=True,
                              db_index=True, null=True)

    # Main
    TEAM_APPLICATION = 'application'
    TEAM_MOBILE_CONTENT = 'mobile content'
    TEAM_VIDEO = 'video'
    TEAM_CHOICES = (
        (TEAM_APPLICATION, _('Application')),
        (TEAM_MOBILE_CONTENT, _('Mobile Content')),
        (TEAM_VIDEO, _('Video')),
    )
    team = models.CharField(_('Team'), choices=TEAM_CHOICES, max_length=255,
                            blank=True, null=True)
    name = models.CharField(_('Name'), max_length=255,
                            blank=True, null=True)
    phone_number = PhoneNumberField(_('Phone number'),
                                    blank=True, null=True)
    skype_id = models.CharField(_('skype id'), max_length=255,
                                blank=True, null=True)
    financial_email = models.EmailField(_('financial email'),
                                        blank=True, null=True)

    # Specific
    document = models.FileField(blank=True, null=True,
                                validators=[validate_pdf_ext],
                                upload_to='documents/%Y/%m/%d')
    legal_entity_name = models.CharField(_('Legal Entity Name'), max_length=255,
                                         blank=True, null=True)
    contact_point = models.CharField(_('Point of contact'), max_length=255,
                                     blank=True, null=True)
    manager = models.ForeignKey('users.User', on_delete=models.SET_NULL,
                                related_name='managed_suppliers',
                                blank=True, null=True)
    publisher = models.ForeignKey('users.User', on_delete=models.SET_NULL,
                                  related_name='user_publishers',
                                  related_query_name='user_publisher',
                                  blank=True, null=True)

    date_joined = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.email

    class Meta:
        db_table = 'advertisers'
