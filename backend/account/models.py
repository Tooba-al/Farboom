import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone



class CustomUserManager(UserManager):
    def _create_user(self, first_name, last_name, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    # def create_user(self, first_name=None, last_name=None, email=None, password=None, **extra_fields):
    #     # extra_fields.setdefault('is_staff', False)
    #     # extra_fields.setdefault('is_superuser', False)
    #     return self._create_user(first_name, last_name, email, password, **extra_fields)
    
    # def create_superuser(self, first_name=None, last_name=None, email=None, password=None, **extra_fields):
    #     # extra_fields.setdefault('is_staff', True)
    #     # extra_fields.setdefault('is_superuser', True)
    #     return self._create_user(first_name, last_name, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255, blank=True, default='')
    last_name = models.CharField(max_length=255, blank=True, default='')

    projects_count = models.IntegerField(default=0)
    # is_active = models.BooleanField(default=True)
    # is_superuser = models.BooleanField(default=False)
    # is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

