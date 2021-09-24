# import uuid

# from django.contrib.auth.models import (
#     AbstractBaseUser,
#     BaseUserManager,
#     PermissionsMixin,
# )
# from django.core.mail import send_mail
# from django.db import models
# from django.utils.translation import gettext_lazy as _
# from django_countries.fields import CountryField


# class CustomAccountManger(BaseUserManager):
#     # custom account manager to manage the user and superuser

#     def create_superuser(self, email, name, password, **other_fields):
#         other_fields.setdefault("is_staff", True)
#         other_fields.setdefault("is_superuser", True)
#         other_fields.setdefault("is_active", True)

#         if other_fields.get("is_staff") is not True:
#             raise ValueError("Superuser must be assigned to is_staff=True.")
#         if other_fields.get("is_superuser") is not True:
#             raise ValueError("Superuser must be assigned to is_superuser=True.")

#         return self.create_user(email, name, password, **other_fields)

#     # we need these fields to populate for superuser now user_name will be replaced by email
#     # USERNAME_FIELD = 'email' REQUIRED_FIELDS = ['user_name']

#     def create_user(self, email, name, password, **otherfields):

#         if not email:
#             raise ValueError(_("Youst must provide email address"))

#         email = self.normalize_email(email)
#         # after validating the fields where things r entering the properly
#         # user = self.model(email=email, user_name=name, **otherfields)
#         user = self.model(email=email, name=name, **otherfields)

#         user.set_password(password)
#         user.save()
#         return user


# # class UserBase(AbstractBaseUser, PermissionsMixin):
# class Customer(AbstractBaseUser, PermissionsMixin):

#     email = models.EmailField(_("email address"), unique=True)
#     name = models.CharField(max_length=150, unique=True)
#     mobile = models.CharField(max_length=10, blank=True)
#     ##USER STATUS - we dont user to get delete we can disable the user to save the user's data
#     is_active = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     # # Delivery details
#     # country = CountryField()
#     # phone_number = models.CharField(max_length=10, blank=True)
#     # address_line_1= models.CharField(max_length=150, blank=True)
#     # address_line_2 = models.CharField(max_length=150, blank=True)
#     # post_code = models.CharField(max_length=7, blank=True)
#     # town_city = models.CharField(max_length=150, blank=True)

#     # #USER STATUS - we dont user to get delete we can disable the user to save the user's data
#     # is_active = models.BooleanField(default=False)
#     # is_staff = models.BooleanField(default=False)

#     # custom account manager to manage the user and superuser
#     objects = CustomAccountManger()
#     # for custom account manager
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ["name"]  # username mandatory

#     class Meta:
#         verbose_name = "Accounts"
#         verbose_name_plural = "Accounts"

#     # for email used in views
#     def email_user(self, subject, message):
#         send_mail(
#             subject,
#             message,
#             "l@1.com",
#             [self.email],
#             fail_silently=False,
#         )

#     def __str__(self):
#         return self.name


# # creating it separate table for the customer each customer will have many addresss


# class Address(models.Model):
#     """ "
#     Address
#     here we use UUIDField to create a long unique string in the id rather than having something like
#     127.0.0.1/edit_details/1/ -this will be easily can be accessed by seeing the id
#     127.0.0.1/edit_details/e1cf1aa9-28f3-4ed2-8f99-fd375384007d/
#     """

#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     customer = models.ForeignKey(Customer, verbose_name=_("Customer"), on_delete=models.CASCADE)
#     full_name = models.CharField(_("Full Name"), max_length=150)
#     phone = models.CharField(_("Phone Number"), max_length=50)
#     postcode = models.CharField(_("Postcode"), max_length=50)
#     address_line = models.CharField(_("Address Line 1"), max_length=255)
#     address_line2 = models.CharField(_("Address Line 2"), max_length=255)
#     town_city = models.CharField(_("Town/City/State"), max_length=150)
#     delivery_instructions = models.CharField(_("Delivery Instructions"), max_length=255)
#     created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
#     updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
#     default = models.BooleanField(_("Default"), default=False)

#     class Meta:
#         verbose_name = "Address"
#         verbose_name_plural = "Addresses"

#     def __str__(self):
#         return "Address"

import uuid

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, name, password, **other_fields)

    def create_user(self, email, name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user


class Customer(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=150)
    mobile = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        verbose_name = "Accounts"
        verbose_name_plural = "Accounts"

    def email_user(self, subject, message):
        send_mail(
            subject,
            message,
            'l@1.com',
            [self.email],
            fail_silently=False,
        )

    def __str__(self):
        return self.name

class Address(models.Model):
    """
    Address
   here we use UUIDField to create a long unique string in the id rather than having something like
   127.0.0.1/edit_details/1/ -this will be easily can be accessed by seeing the id
   127.0.0.1/edit_details/e1cf1aa9-28f3-4ed2-8f99-fd375384007d/ -this is the use of uuid  
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, verbose_name=_("Customer"), on_delete=models.CASCADE)
    full_name = models.CharField(_("Full Name"), max_length=150)
    phone = models.CharField(_("Phone Number"), max_length=50)
    postcode = models.CharField(_("Postcode"), max_length=50)
    address_line = models.CharField(_("Address Line 1"), max_length=255)
    address_line2 = models.CharField(_("Address Line 2"), max_length=255)
    town_city = models.CharField(_("Town/City/State"), max_length=150)
    delivery_instructions = models.CharField(_("Delivery Instructions"), max_length=255)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    default = models.BooleanField(_("Default"), default=False)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return "Address"
