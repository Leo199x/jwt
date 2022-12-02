from lib2to3.pytree import Base
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Must have an email address')

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(
            email,
            password,
            **extra_fields
        )
        user_is_staff = True
        user_is_superuser = True
        user.save(using=self._db)
        return user