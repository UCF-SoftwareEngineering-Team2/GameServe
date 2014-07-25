from django.db import models
from django.db.models import Q
from profile.models import User
from django.utils import timezone
from datetime import datetime
from dateutil.relativedelta import relativedelta





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
        return self.filter( dateTime__gte = timezone.datetime.now())

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



class Event(models.Model):
    objects = EventManager()



    ###################################################################################
    #                                Fields 
    ###################################################################################
    dateTime = models.DateTimeField(auto_now=False)
    endTime = models.DateTimeField(auto_now=False)
    duration = models.FloatField()

    creator = models.ForeignKey(User,related_name='creator')
    court = models.ForeignKey(Court, related_name='court')
    participants = models.ManyToManyField(User,related_name='participants')

    gameHeat = 0 #models.IntegerField(default=0)
    numComments = 0 #models.IntegerField()
    checkIns = 0 #models.IntegerField()
    # duration = models.DateTimeField(auto_now=False)

    def __unicode__(self):
        return u'%s' % (self.dateTime)



    ###################################################################################
    #                                Model Methods 
    ###################################################################################
    def set_creator(self, user):
        if ( not self.creator ):
            self.creator = user
            self.add_participant(user)
        else:
            print 'replacing creator'
            self.remove_participant(self.creator)
            self.creator = user
            
    def add_participant(self, user):
        if type(user).__name__ == 'User':
            self.participants.add(user)
        elif type(user).__name__ == 'int':
            self.participants.add(User.objects.get(id=user))
        else:
            raise ValueError("Incorrect Args")

    def remove_participant(self, user):
        if type(user).__name__ == 'int':
            self.participants.remove(self.participants.get(id=user))
        elif type(user).__name__ == 'User':
            self.participants.remove(user)
        else:
            raise ValueError("Incorrect Args")



    ###################################################################################
    #                                Properties 
    ###################################################################################

    # Sets the mins until this event begins as a property. You do the math if you gotta.
    # Set as -1 if already event already past
    @property
    def timeUntil(self):
        if not self.isUpcoming:
            return -1
        else: 
            rd = relativedelta(self.dateTime, timezone.now())
            return {'days':rd.days, 'minutes':rd.minutes, 'seconds':rd.seconds}

    # Instance method
    @property
    def isUpcoming(self):
        td = self.dateTime - timezone.now()
        if ( td.days >= 0 and td.seconds > 0 ):
            return True
        else:
            return False

    class Meta:
        ordering = ('dateTime',)

