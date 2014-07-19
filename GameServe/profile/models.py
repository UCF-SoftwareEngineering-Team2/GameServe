from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# accounts.models.User extends django.contrib.auth.models.User
# class nUser(User):
#     phone_number = models.CharField(default='',max_length=10)
#     reputation = models.IntegerField(default=0)

#     # Override the __unicode__() method to return out something meaningful!
#     def __unicode__(self):
#         return self.user.username



class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        """
        Creates and saves a User with the given email,
        username and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
        	raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username = username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
            username=username,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    objects = UserManager()

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    username = models.CharField(unique=True, max_length=20, verbose_name='username')

    phone_number = models.CharField(default='',max_length=10)
    reputation = models.IntegerField(default=0)


    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'						# User email as the username
    REQUIRED_FIELDS = ['username']




    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin