import random, string

from django.conf import settings
from django.http import HttpRequest, QueryDict
from django.utils.importlib import import_module

from allauth.account import signals
from allauth.account.forms import SignupForm






'''
    AllAuth Utilities

    Utilities for manual creation of allauth.account.model.EmailAddress entry which has a foreign Key
    relation to profile.models.User object.  
    
    Creation of EmailAddress object results in creation of profile.User object
    
    Usage: 
        create_allauth_user(email='myemail@blahblah.com', username='iamJames', password='randomGeneratedIfEmpty')
'''
def generate_password(chars=8):
    """ Used for generating a random password if none is supplied """
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(chars))


def get_post_dic(email, username, password):
    """ Creates a dictionary with given params """
    password = generate_password() if (password == '') else password
    #csrfmiddlewaretoken = #not necessary
    return {
            #u'csrfmiddlewaretoken': #not necessary
            u'email': email,
            u'username':username,
            u'password1': password,
            u'password2': password,
            u'confirmation_key': ""
    }
def get_signin_request(post_dic):
    signin_request = HttpRequest()

    query_dict = QueryDict("")
    query_dict_post = query_dict.copy() # Make it mutable
    query_dict_get = query_dict.copy()  # Make it mutable

    query_dict_post.update(post_dic)

    signin_request.POST = query_dict_post
    signin_request.GET = query_dict_get

    # Set session (fails without)
    # http://stackoverflow.com/questions/16865947/django-httprequest-object-has-no-attribute-session
    engine = import_module(settings.SESSION_ENGINE)
    session_key = None
    signin_request.session = engine.SessionStore(session_key)

    signin_request.SERVER_NAME = ""

    return signin_request


def create_allauth_user(email, username, password='', phonenumber='' ):
    # Create dictionary with given required params to generate signin_request
    post_dic = get_post_dic(email, username, password)
    # Generate signin_request that contains dictionary in POST params
    signin_request = get_signin_request(post_dic)

    # POST data as kwargs for signupForm
    signup_form_kwargs = {"files": {}, "initial": {},
                          "data": signin_request.POST}

    # SignUpForm Instatiation with post data 
    # makes SignupView.form_valid method activate
    signup_form = SignupForm(**signup_form_kwargs)
    signup_form.cleaned_data = post_dic              # Csrf token not neccesary either

    # Generates a user object from the form data
    user = signup_form.save(signin_request)
    # If phone number supplied add it to the model
    user.phone_number = phonenumber
    user.save()

    # Sends allauth.signed_up signal
    signals.user_signed_up.send(sender=user.__class__,
                                request=signin_request,
                                user=user,
                                signal_kwargs={})
    return user



# With `ACCOUNT_AUTHENTICATION_METHOD = "email"`
#allauth_regular_user = create_allauth_user("my_email@gmail.com")