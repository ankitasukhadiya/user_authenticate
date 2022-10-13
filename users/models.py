from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    # username = None
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length = 20)
    email = models.EmailField(_('email address'),max_length=50,unique=True)
    password = models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20)
    
    USEREMAIL_FIELD = 'email'
    REQUIRED_FIELDS =  []
    objects = UserManager()
