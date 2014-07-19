from django.contrib import admin
from accounts.models import User
from django.contrib.auth.admin import UserAdmin

# admin.site.unregister(User)





class UserInline(admin.StackedInline):
  model = User

class UserAdmin(UserAdmin):
  def phone_number(self, obj):
    try:
      return obj.get_profile().phone_number
    except User.DoesNotExist:
      return 'N/A'
  def reputation(self, obj):
    try:
      return obj.get_profile().reputation
    except User.DoesNotExist:
      return 'N/A'

  list_display = ('email','username','phone_number','reputation','date_joined')
  search_fields = UserAdmin.search_fields + ('user__phone_number','user__reputation',)


UserAdmin.list_display = ('email','first_name',)
admin.site.register(User, UserAdmin)