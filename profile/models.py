from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from allauth.socialaccount.models import SocialAccount
import hashlib


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
 
        user = self.model(email = self.normalize_email(email),
                          username = username)
        
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_superuser(self, email, username, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email, password=password,
                                       username=username )
        user.is_admin = True
        user.save(using=self._db)
        return user
 
 
class User(AbstractBaseUser):
    """
        Defines the user model fields and relation
    """
 
    # Custom managers add table-wide functionality to the model
    objects = UserManager()
 
 
    ###################################################################################
    #                                Fields 
    ###################################################################################
    # User email address (required)
    email    = models.EmailField(blank=False, 
                                 unique = True, 
                                 max_length = 40, 
                                 verbose_name = 'email')
    # User's username (required)
    username = models.CharField(unique=True, 
                                blank=False,
                                max_length = 20, 
                                verbose_name = 'username')
 
    # Extra profile information 
    phone_number = models.CharField(default = '',
                                    max_length = 10,
                                    verbose_name='phonenumber')

    reputation   = models.IntegerField(default = 0)


    numCommits = 0 #models.IntegerField(blank=False)
    numComments = 0 #models.IntegerField(default = 0)
    numCheckIns = 0 #models.IntegerField(default = 0)

    # Required definitions for overriding default user model
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
 
 
    USERNAME_FIELD = 'email'                # User email as the username
    REQUIRED_FIELDS = ['username']          # Require the username and email fields
 
 
    class Meta:
        db_table = 'usertable'
        
 
    ###################################################################################
    #                                Methods 
    ###################################################################################
 

    # @Override 
    def get_full_name(self):
        # The user is identified by their email address
        return self.email
 
    # @Override 
    def get_short_name(self):
        # The user is identified by their email address
        return self.email
 
    # @Override 
    def __str__(self):              # __unicode__ on Python 2
        return self.email
 
    # @Override 
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
 
    # @Override 
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
 
    def profile_image_url(self):
        ''' Returns link to facebook profile image for those who are logged in via facebook '''
        fb_uid = SocialAccount.objects.filter(user_id=self.id, provider='facebook')
        if len(fb_uid):
            return "http://graph.facebook.com/{}/picture?width=120&height=120".format(fb_uid[0].uid)
 
        return "http://www.gravatar.com/avatar/{}?s=40".format(hashlib.md5(self.email).hexdigest())
        
    def facebook_profile(self):
        fb_uid = SocialAccount.objects.filter(user_id=self.id, provider='facebook')
        if len(fb_uid):
            return True
        return False
    ###################################################################################
    #                                Properties 
    ###################################################################################
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin




