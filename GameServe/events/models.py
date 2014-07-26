from django.db import models
from django.db.models import Q
from profile.models import User
from django.utils import timezone
import datetime




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


    def create_event(self, dateTime, creator, court, duration):

        # Check if event either starts during the time period, ends during the time period, 
        # or starts before and ends after the time period.
        def occuring_during(court, start, end):
            return Event.objects.filter(Q(court=court), 
                Q(Q(dateTime__range=[start, end]) | Q(endTime__range=[start,end]) |
                    Q(Q(dateTime__lte=start), Q(endTime__gte=end))))

        # Create dt (start) and dte (end) times
        dt = datetime.datetime.fromtimestamp(float(dateTime))
        dte = datetime.datetime.fromtimestamp(float(dateTime) + float(duration))

        #Get instance of court it will be occuring on
        courtInstance = Court.objects.get(pk=court)

        #Return error, otherwise, return created event instance
        if(occuring_during(court=courtInstance, start=dt, end=dte)):
            return 'Error, court taken during this time.'
        else:
            event = self.create(dateTime=dt, endTime=dte, creator=User.objects.get(pk=creator), court=courtInstance, duration=duration)
            return event;

    def add_participant(self, user, event):
        # Get event by id
        eventInstance = Event.objects.get(pk=event)

        # Add user to participants
        eventInstance.participants.add(User.objects.get(pk=user))
        return eventInstance

    def remove_participant(self, user, event):
        # Get event by id
        eventInstance = Event.objects.get(pk=event)

        # If user exists in participants, remove them
        if(eventInstance.participants.filter(id=user) is not None):
            eventInstance.participants.remove(User.objects.get(pk=user))
            return eventInstance
        else:
            return 'No such participant'



class Event(models.Model):
    objects = EventManager()
    dateTime = models.DateTimeField(auto_now=False)
    endTime = models.DateTimeField(auto_now=False)
    duration = models.FloatField()

    creator = models.ForeignKey(User,related_name='creator')
    court = models.ForeignKey(Court, related_name='court')
    participants = models.ManyToManyField(User,related_name='participants')
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

