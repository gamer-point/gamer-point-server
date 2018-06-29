from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    Tells Django to work with our custom user model.
    """
    
    def create_user(self, email, first_name, last_name, password=None):
        """
        Create a new user object
        :param email: the email
        :param first_name: the user first name
        :param last_name: the user last name
        :param password: the user raw password
        :return: user object
        """
        if not email:
            raise ValueError('User must have an email')
        
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email, first_name, last_name, password=None):
        """
        Create a new super user
        :param email: the email
        :param first_name: the user first name
        :param last_name: the user last name
        :param password: the user raw password
        :return: user object
        """
        
        user = self.create_user(email, first_name, last_name, password)
        user.is_superuser = True
        user.is_staff = True
        
        user.save(using=self._db)
        
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Represent an user inside the Gamer Point
    """
    
    class Meta:
        db_table = 'gp_users'
    
    first_name = models.CharField(max_length=60)
    middle_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    username = models.CharField(max_length=60, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    mobile = models.CharField(max_length=64, null=True, blank=True, default=None)
    is_tfa_enabled = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_mobile_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    
    """
    A list of fields required when creating an user via `createsuperuser`
    """
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'password']
    
    def get_full_name(self):
        """
        Use to get the user full name.
        :return: string
        """
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name
    
    def get_short_name(self):
        """
        Use to get the user's name without middle name.
        :return: string
        """
        return self.first_name + ' ' + self.last_name
    
    def __str__(self):
        """
        Django uses this when it needs to convert the object to a string
        :return: string
        """
        return self.email
