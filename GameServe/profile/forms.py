from profile.models import User
from django import forms
from profile.validator import validate_email_unique
#from allauth.account.forms import BaseSignupForm


class RegisterForm(forms.Form):
    
    password1 = forms.PasswordInput()
    phone_number = forms.CharField(max_length=13,
                                   required = False,
                                   widget=forms.TextInput(attrs={'class':'loginField'}))
    def save(self, user):
        if 'phone_number' in self.data:
            user.phone_number = self.data['phone_number']
            user.save()

                             
        
        
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(required = True, validators = [validate_email_unique])

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

# class UserProfileForm(forms.ModelForm):
#     phone_number = forms.CharField(max_length=10, min_length=0)
#     class Meta:
#         model = UserProfile
#         fields = ('phone_number', )
