import uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def create_superuser(self, username, password, **kwargs):
        account = self.create_user(username, password, **kwargs)
        account.is_admin = True
        account.is_staff = True
        account.is_superuser = True
        account.save()
        return account

class User(PermissionsMixin, AbstractBaseUser):
    USERNAME_FIELD = 'username'
    username_validator = UnicodeUsernameValidator()
    objects = UserManager()
    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number must be exactly 10 digits.")
    phone = models.CharField(max_length=10, validators=[phone_regex], null=True)
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    full_name = models.CharField(_("first name"), max_length=150, blank=True, null=True)
    email = models.EmailField(_("email address"), unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    address = models.TextField(null=True, blank=True)
    college = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.username:
            email_base = self.email.split('@')[0]
            unique_identifier = uuid.uuid4().hex[:4]
            self.username = f"{email_base}_{unique_identifier}"
        super(User, self).save(*args, **kwargs)

