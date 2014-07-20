from django.db import models
from profile.models import User
from django.utils import timezone




class SportManager(models.Manager):
    pass

class Sport(models.Model):
    objects = SportManager()
    sportType = models.CharField(unique=True,max_length=10)

    def __unicode__(self):
        return u'%s'%self.sportType








class CourtManager(models.Manager):
    def scheduledNext( self, courtID ):
        try:
            upcoming = self.events.filter( upcoming = self.filter( dateTime__gte = timezone.datetime.now()))[0]
            return upcoming
        except( Court.DoesNotExist ):
            return

class Court(models.Model):
    objects = CourtManager()

    sport = models.ForeignKey(Sport, related_name='sport')
    latitude = models.FloatField()
    longitude = models.FloatField()

    def getNextScheduled(self,page=1):
        return self.events.upcomingEvent()[(page-1)*5:(page)*5]


    def __unicode__(self):
        return u'%s (%s, %s)' % (self.sport.sportType, self.latitude, self.longitude)
    class Meta:
        ordering = ('sport',)











class EventManager(models.Manager):

    def upcoming(self):
        return self.filter( dateTime__gte = timezone.datetime.now() )


class Event(models.Model):
    objects = EventManager()
    dateTime = models.DateTimeField(auto_now=False)
    creator = models.ForeignKey(User,related_name='creator')
    court = models.ForeignKey(Court, related_name='court')
    participants = models.ManyToManyField(User,related_name='participants')
    gameHeat = 0 #models.IntegerField(default=0)
    numComments = 0 #models.IntegerField()
    checkIns = 0 #models.IntegerField()
    # duration = models.DateTimeField(auto_now=False)

    def __unicode__(self):
        return u'%s' % (self.dateTime)

    # Instance method
    def upcomingEvent(self):
        date = self.dateTime.date()
        time = self.dateTime.time()
        newDay=date.day+1 if (time.hour+2 > 23) else date.day

        extTime = timezone.datetime(month=date.month, day=newDay,
                                    year=date.year, hour=(time.hour+2)%24,
                                    minute=time.minute)
        now = timezone.datetime.now()
        curTime = now.time()
        curDate = now.date()

        # If this event is days away
        if ( date > curDate ):
            return True
        elif ( date == curDate ):
            # if hours or minutes away from current time
            if ( time > curTime or  extTime > curTime ):
                return True
            else:
                return False
        else:
            return False
    upcomingEvent.short_description = "Is this event upcoming?"
    upcoming = property(upcomingEvent)

    class Meta:
        ordering = ('dateTime',)

