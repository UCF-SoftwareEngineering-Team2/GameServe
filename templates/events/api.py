from profile.models import User
from events.models import Court, Event, Sport
from GameServe.serializers import PrettyJSONSerializer
from tastypie.constants import ALL
from tastypie.authorization import DjangoAuthorization
from tastypie.utils import timezone
from tastypie.resources import ModelResource
from tastypie import fields

# TODO: Get tastype user creation working
class UserResource(ModelResource):
    participation = fields.ToManyField('events.api.EventResource', 'participants', null=True, blank=True)
    creatorOf = fields.ToManyField('events.api.EventResource', 'creator', null=True, blank=True)
    username = fields.CharField(attribute='username')

    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['username','email','creatorOf', 'participation']
        allowed_methods = ['get','post','put']
        # Serialize into pretty-printed json
        serializer = PrettyJSONSerializer()
       
        filtering = {
            'participation':ALL,
            'creator':ALL,
            'username':ALL
        }
        authorization = DjangoAuthorization()

    # Default return format
    def determine_format( self, request):
        return 'application/json'



'''
    To add to sport model via REST api

    data = JSON.stringify({"sportType":"Quidditch"})
    $.ajax({
        url: 'http://localhost:8000/api/v1/sport/',
        type: 'POST',
        contentType: 'application/json',
        data: data,
        dataType: 'json',
        processData: false
    })
'''
# Note: Tested
class SportResource(ModelResource):
    courts = fields.ToManyField('events.api.CourtResource', 'courts', null=True, blank=True)
    
    class Meta:
        queryset = Sport.objects.all()
        resource_name = 'sport'
        fields =['sportType', 'court']
        allowed_methods = ['get','post','put']
        # Serialize into pretty-printed json
        serializer = PrettyJSONSerializer()

        authorization = DjangoAuthorization()


    # Default return format
    def determine_format( self, request):
        return 'application/json'





''' Example Ajax POST 

    data = JSON.stringify({"sport":"/api/v1/sport/3/", 
                          "latitude":"12.3828", 
                          "longitude":"12.292999" })
    $.ajax({
        url: 'http://localhost:8000/api/v1/court/',
        type: 'POST',
        contentType: 'application/json',
        data: data,
        dataType: 'json',
        processData: false
    })
'''
# Note: Tested
class CourtResource(ModelResource):
    sport = fields.ToOneField(SportResource, 'sport')
    longitude = fields.FloatField(attribute='longitude')
    latitude = fields.FloatField(attribute='latitude')
    class Meta:
        queryset = Court.objects.all()
        resource_name = 'court'
        allowed_methods = ['get','post','put']
        fields = ['latitude','longitude','sport']
        allowed_methods = ['get','post','put']
        # Serialize into pretty-printed json
        serializer = PrettyJSONSerializer()
        
        filtering = {
            'sport':ALL
        }
        authorization = DjangoAuthorization()

    # Default return format
    def determine_format( self, request):
        return 'application/json'




# TODO: Get event creation via Tastypie working.
class EventResource(ModelResource):
    # 'creator' refers to the variable name in models.p
    creator = fields.ToOneField(UserResource,'creator')
    participants = fields.ManyToManyField(UserResource, 'participants',null=True,blank=True)
    court = fields.ToOneField(CourtResource, 'court')

    # timeUntil = fields.CharField(attribute='timeUntil', readonly=True)
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'event'
        fields = ['dateTime','attending','creator','court']
        allowed_methods = ['get','post','put']
        # Serialize into pretty-printed json
        serializer = PrettyJSONSerializer()
        
        filtering = {
            'dateTime':['lte','gte',],
            'court':ALL,
            'court_sport_sportType':ALL,
        }
        authorization = DjangoAuthorization()

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

 
