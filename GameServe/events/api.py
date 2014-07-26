from tastypie.resources import ModelResource
from tastypie import fields
from profile.models import User
from events.models import Court, Event, Sport
from GameServe.serializers import PrettyJSONSerializer
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.utils import timezone

class UserResource(ModelResource):
    participation = fields.ToManyField('events.api.EventResource', 'participants', null=True, blank=True)
    creatorOf = fields.ToManyField('events.api.EventResource', 'creator', null=True, blank=True)
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['username','email','creatorOf']
        # Serialize into pretty-printed json
        serializer = PrettyJSONSerializer()
        filtering = {
            'attends':ALL,
            'creator':ALL,
            'username':ALL
        }
    # Default return format
    def determine_format( self, request):
        return 'application/json'

class SportResource(ModelResource):
    court = fields.ToManyField('events.api.CourtResource', 'sport', null=True, blank=True)
    class Meta:
        queryset = Sport.objects.all()
        resource_name = 'sport'
        fields =['sportType']
        # Serialize into pretty-printed json
        serializer = PrettyJSONSerializer()

    # Default return format
    def determine_format( self, request):
        return 'application/json'


class CourtResource(ModelResource):
    sport = fields.ToOneField(SportResource, 'sport')
    class Meta:
        queryset = Court.objects.all()
        resource_name = 'court'
        allowed_methods = ['get']
        fields = ['latitude','longitude']

        # Serialize into pretty-printed json
        serializer = PrettyJSONSerializer()
        filtering = {
            'sport':ALL
        }
    # Default return format
    def determine_format( self, request):
        return 'application/json'

class EventResource(ModelResource):
    # 'creator' refers to the variable name in models.p
    creator = fields.ToOneField(UserResource,'creator')
    participants = fields.ManyToManyField(UserResource, 'participants',null=True,blank=True)
    court = fields.ToOneField(CourtResource, 'court')

    timeUntil = fields.CharField(attribute='timeUntil', readonly=True)
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'event'
        fields = ['dateTime','attending','creator','court','timeUntil']

        # Serialize into pretty-printed json
        serializer = PrettyJSONSerializer()
        filtering = {
            'dateTime':['lte','gte',],
            'court':ALL,
            'court_sport_sportType':ALL,
            'timeUntil':ALL 
        }

    # Default return format
    def determine_format( self, request):
        return 'application/json'

    def build_filters(self, filters=None):
        """
        Build additional filters
        """
        if not filters:
            filters = {}
        orm_filters = super(EventResource, self).build_filters(filters)

        if 'upcoming__gte' in filters:
            upcoming = filters['upcoming__gte']
            orm_filters['upcoming'] = 'gte'

        return orm_filters

    def apply_filters(self, request, applicable_filters):
        """
        Apply the filters
        """
        if 'upcoming' in applicable_filters:
            d = applicable_filters.pop('upcoming')
            up = Event.objects.filter(dateTime__gte = timezone.now())
            applicable_filters['upcoming'] = up
        return super(EventResource, self).apply_filters(request, 
                                                        applicable_filters)

    # def build_filters(self, filters=None):
    #     """
    #     Build additional filters
    #     """
    #     if not filters:
    #         filters = {}
    #     orm_filters = super(EventResource, self).build_filters(filters)

    #     if 'event__upcoming' in filters:
    #         # import ipdb; ipdb.set_trace()
    #         orm_filters['upcoming'] = filters['event__upcoming']
    #     return orm_filters

    # def apply_filters(self, request, applicable_filters):
    #     """
    #     Apply the filters
    #     """
    #     if 'upcoming' in applicable_filters:
    #         upcoming = applicable_filters.pop('upcoming')
    #         #import ipdb; ipdb.set_trace()
    #         upcoming = [ up.strip() for up in upcoming.split(',') ]
    #         applicable_filters['event__upcoming'] = upcoming
    #     return super(EventResource, self).apply_filters(request, applicable_filters)