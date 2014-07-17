from tastypie.resources import ModelResource
from tastypie import fields

from accounts.models import User
from events.models import Court, Event, Sport

from GameServe.serializers import PrettyJSONSerializer

import datetime

class UserResource(ModelResource):
    #attends = fields.ToManyField('events.api.EventResource', 'attends',null=True,blank=True)
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['username','email']
        serializer = PrettyJSONSerializer()
    def determine_format( self, request):
        return 'application/json'

class SportResource(ModelResource):
    class Meta:
        queryset = Sport.objects.all()
        resource_name = 'sport'
        fields =['sportType']
        serializer = PrettyJSONSerializer()
    def determine_format( self, request):
        return 'application/json'

class CourtResource(ModelResource):
    sport = fields.ToOneField(SportResource, 'sport')
    class Meta:
        queryset = Court.objects.all()
        resource_name = 'court'
        allowed_methods = ['get']
        fields = ['latitude','longitude']
        serializer = PrettyJSONSerializer()
    def determine_format( self, request):
        return 'application/json'

class EventResource(ModelResource):
    # 'creator' refers to the variable name in models.p
    creator = fields.ToOneField(UserResource,'creator')

    participants = fields.ManyToManyField(UserResource, 'participants',null=True,blank=True)

    court = fields.ToOneField(CourtResource, 'court')
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'event'
        fields = ['dateTime','attending','creator','court']
        serializer = PrettyJSONSerializer()

    def build_filters(self, filters=None):
        """
        Build additional filters
        """
        if not filters:
            filters = {}
        orm_filters = super(EventResource, self).build_filters(filters)

        if 'event__upcoming' in filters:
            upcoming = filters['event__upcoming']
            orm_filters['upcoming'] = upcoming
        return orm_filters

    def apply_filters(self, request, applicable_filters):
        """
        Apply the filters
        """
        if 'upcoming' in applicable_filters:
            upcoming = applicable_filters.pop('upcoming')
            upcoming = [ up.strip() for up in upcoming.split(',') ]

            applicable_filters['event__upcoming'] = upcoming
        return super(EventResource, self).apply_filters(request,
                                                        applicable_filters)
    def determine_format( self, request):
        return 'application/json'
