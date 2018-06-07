from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, BaseUserManager
from django.utils.translation import ugettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

from core.utils import uuid_hex
from core.validators import validate_pdf_ext


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=32, default=uuid_hex(),
                                blank=False, unique=True)
    email = models.EmailField(_('email'), max_length=254, unique=True,
                              db_index=True, null=True)

    # Detail User info
    first_name = models.CharField(_('first name'), max_length=64)
    last_name = models.CharField(_('last name'), max_length=64)
    avatar = models.ImageField(_('Avatar'), blank=True, null=True,
                               upload_to='avatars/%Y/%m/%d')

    # Main
    ROLE_ADMIN = 'admin'
    ROLE_EMPLOYEE = 'employee'
    ROLE_PUBLISHER = 'publisher'
    ROLE_CHOICES = (
        (ROLE_ADMIN, _('Admin')),
        (ROLE_EMPLOYEE, _('Employee')),
        (ROLE_PUBLISHER, _('Publisher')),
    )
    role = models.CharField(_('role'), max_length=254, null=True,
                            choices=ROLE_CHOICES, default=ROLE_ADMIN)
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

    # Publisher specific
    document = models.FileField(blank=True, null=True,
                                validators=[validate_pdf_ext],
                                upload_to='documents/%Y/%m/%d')
    legal_entity_name = models.CharField(_('Legal Entity Name'), max_length=255,
                                         blank=True, null=True)
    contact_point = models.CharField(_('Point of contact'), max_length=255,
                                     blank=True, null=True)
    manager = models.ForeignKey('users.User', on_delete=models.SET_NULL,
                                related_name='user_managers',
                                blank=True, null=True)
    advertiser = models.ForeignKey('users.User', on_delete=models.SET_NULL,
                                   related_name='user_advertisers',
                                   blank=True, null=True)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user '
                    'can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    date_joined = models.DateField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users'
        ordering = ['-date_joined']
