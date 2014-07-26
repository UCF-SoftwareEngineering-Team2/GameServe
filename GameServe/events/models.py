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

    # TODO: Determine in instance-level method bettern than table-wide method for remove/add participants
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
        ''' Adds given instance of user, or given id of user to participants'''
        if type(user).__name__ == 'int':
            uid = user
        elif type(user).__name__ == 'User':
            uid = user.id
        else:
            raise ValueError("Incorrect Args")

        if (self.participants.filter(id=uid).count() > 0):
             self.participants.add(self.participants.filter(id=uid))
             return self 
        else: 
            return 'User with id#: %d does not exist'%uid


    def remove_participant(self, user):
        ''' Removes given user or user id from participants or ValueError'''
        if type(user).__name__ == 'int':
            uid = user
        elif type(user).__name__ == 'User':
            uid = user.id
        else:
            raise ValueError("Incorrect Args")

        if (self.participants.filter(id=uid).count() > 0):
             self.participants.remove(self.participants.filter(id=uid))
             return self 
        else: 
            return 'No such participant'

    def get_time_until(self):
        ''' Returns the time until this event begins as a dictionary object '''
        if not self.isUpcoming:
            return -1
        else: 
            rd = relativedelta(self.dateTime, timezone.now())
            return {'days':rd.days, 'minutes':rd.minutes, 'seconds':rd.seconds}





    ###################################################################################
    #                                Properties 
    ###################################################################################

    # Sets the mins until this event begins as a property. You do the math if you gotta.
    # Set as -1 if already event already past
    @property
    def isUpcoming(self):
        td = self.dateTime - timezone.now()
        if ( td.days >= 0 and td.seconds > 0 ):
            return True
        else:
            return False
            
    @property
    def timeUntil(self):
        if not self.isUpcoming:
            return -1
        else: 
            rd = relativedelta(self.dateTime, timezone.now())
            return {'days':rd.days, 'minutes':rd.minutes, 'seconds':rd.seconds}

    # Instance method

    class Meta:
        ordering = ('dateTime',)

