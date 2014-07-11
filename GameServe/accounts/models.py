from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField

# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, related_name='profile')

    # The additional attributes we wish to include.
    # phone_number = PhoneNumberField()
    phone_number = models.CharField(default='',max_length=10)
    reputation = models.IntegerField(default=0)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
