from django.db import models
from django.contrib.auth.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver

from ..settings.models import *


class UserManagerModel(BaseUserManager):

    def create_user(self, email, username, first_name, last_name, password=None):
        if not email:
            raise ValueError("The email is required")
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            user_type=1
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, first_name, last_name, password):
        user = self.create_user(
            email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.superuser = True
        user.save()
        return user


class UserModel(AbstractBaseUser):
    CUSTOMER = '1'
    EMPLOYEE = '2'
    USER_TYPE = (
        (CUSTOMER, 'CUSTOMER'),
        (EMPLOYEE, 'EMPLOYEE'),
    )

    username = models.CharField('Username', unique=True, max_length=100)
    first_name = models.CharField('First name', max_length=200, blank=True, null=True)
    last_name = models.CharField('Last name', max_length=200, blank=True, null=True)
    email = models.EmailField('Email', max_length=254, unique=True)
    is_active = models.BooleanField(default=True)
    superuser = models.BooleanField(default=False)
    image = models.ImageField('Image', upload_to='images/', max_length=200, blank=True, null=True)
    user_type = models.CharField(choices=USER_TYPE, max_length=1, blank=True, null=True)
    objects = UserManagerModel()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name},{self.last_name}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.superuser

    @property
    def is_activated(self):
        return self.is_active

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         UserModel.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()


