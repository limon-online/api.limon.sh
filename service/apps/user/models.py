from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager

from libs.models import BaseModel


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(
        max_length=64
    )
    last_name = models.CharField(
        max_length=64
    )
    email = models.EmailField(
        unique=True,
        max_length=254
    )
    is_staff = models.BooleanField(
        default=False
    )

    class UserManager(BaseUserManager):
        def _create_user(self, email, password, **kwargs):
            email = self.normalize_email(email)
            user = self.model(email=email, **kwargs)
            user.set_password(password)
            user.save(using=self._db)

            return user

        def create_user(self, email, password, **kwargs):
            kwargs['is_superuser'] = False

            return self._create_user(email, password, **kwargs)

        def create_superuser(self, email, password, **kwargs):
            kwargs['is_superuser'] = True
            kwargs['is_staff'] = True
            kwargs['is_active'] = True
            kwargs.setdefault('first_name', '')
            kwargs.setdefault('last_name', '')

            return self._create_user(email, password, **kwargs)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
