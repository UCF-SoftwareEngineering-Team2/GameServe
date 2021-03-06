from django.contrib import admin
from events.models import Event, Court, Sport, RecentActivity
 
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('court','dateTime','creator','timeUntil','duration')
class CourtAdmin(admin.ModelAdmin):
    list_display = ('sport','latitude','longitude')
 
admin.site.register(Sport)
admin.site.register(Event,EventAdmin)
admin.site.register(Court,CourtAdmin)
admin.site.register(RecentActivity)