from django.contrib import admin

from accounts.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.unregister(User)





class UserProfileInline(admin.StackedInline):
  model = UserProfile

class UserProfileAdmin(UserAdmin):

  def phone_number(self, obj):
    try:
      return obj.get_profile().phone_number
    except UserProfile.DoesNotExist:
      return ''
  def reputation(self, obj):
    try:
      return obj.get_profile().reputation
    except UserProfile.DoesNotExist:
      return ''
      
  list_display = ('email','username','phone_number','reputation','date_joined')
  search_fields = UserAdmin.search_fields + ('profile__phone_number','profile__reputation',)

class UserAdmin(UserAdmin):
  inlines = (UserProfileAdmin,)


UserAdmin.list_display = ('email','first_name',)
admin.site.register(User, UserProfileAdmin)



