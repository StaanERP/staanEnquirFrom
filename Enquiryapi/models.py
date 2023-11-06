from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

status = (
    ("Not Contacted", "Not Contacted"),
    ("Converted", "Converted"),
    ('Junk', "Junk")
)


class Conferencedata(models.Model):
    Name = models.CharField(max_length=50)


class product(models.Model):
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name


class enquiryDatas(models.Model):
    Name = models.CharField(max_length=50)
    OrganizationName = models.CharField(max_length=200)
    Email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits "
                                         "allowed.")
    status = models.CharField(max_length=50, choices=status)
    MobileNumber = models.CharField(validators=[phone_regex], max_length=17)
    Location = models.CharField(max_length=200)
    message = models.CharField(max_length=500, blank=True)
    Interesteds = models.ManyToManyField(product)
    conferencedata = models.ForeignKey(Conferencedata, on_delete=models.SET_NULL, null=True, blank=True)


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    JobRoal = models.CharField(max_length=50, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    def __str__(self):
        return self.user_name
