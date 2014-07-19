from django.db import models
from django.contrib.auth.models import User

# accounts.models.User extends django.contrib.auth.models.User
class User(User):
    phone_number = models.CharField(default='',max_length=10)
    reputation = models.IntegerField(default=0)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

