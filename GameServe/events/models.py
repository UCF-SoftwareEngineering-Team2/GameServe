from django.db import models
from django.contrib.auth.models import User
from accounts.models import UserProfile
import datetime

# Create your models here.
class Sport(models.Model):
    sportType = models.CharField(unique=True,max_length=10)

    def __unicode__(self):
        return u'%s'%self.sportType

# Create your models here.
class Court(models.Model):
    sport = models.ForeignKey(Sport)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __unicode__(self):
        return u'%s (%s, %s)' % (self.sport.sportType, self.latitude, self.longitude)



class Event(models.Model):
    date = models.DateField(auto_now=False)
    time = models.TimeField(auto_now=False)

    court = models.ForeignKey(Court)
    users = models.ManyToManyField(User,related_name='participant')
    creator = models.ForeignKey(User,related_name='creator')

    def __unicode__(self):
        return u'( Sport: %s, Date: %s, Time: %s, Lat/Long: (%s,%s) )' % (self.court.sport.sportType, self.date, self.time, self.court.latitude, self.court.longitude)


    def upcomingEvent(self):
        if (self.date > datetime.date.today()):
            return True
        elif (self.date == datetime.date.today()):
            now = datetime.datetime.now()
            if (self.time >= datetime.datetime.time(datetime.datetime.now()) or datetime.time(hour=self.time.hour+2,minute=self.time.minute) > datetime.datetime.time(datetime.datetime.now()) ):
                return True
            else:
                return False
        else:
            return False
    upcomingEvent.short_description = "Is this event upcoming?"
    upcoming = property(upcomingEvent)

