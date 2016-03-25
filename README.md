## UCF [COP 4331] Software-Engineering Project Page 
-------------------------

- [X] Need all the navigation links looked at. 'Create event' button isn't toggled when create page is the current page.

- [X] Gotta do something about the pop up for the login. I prefer the registration button as one of the navi buttons alongside login, create event, browse, and home; only display login and register for those who aren't logged in.

- [X] Facebook login/registration is working.  Just need a button for it.

- [X] Google Maps Js needs fiddling

- [X] Have to remove unused js files and consolidate short ones into a single js file. Makes cross referencing a pain

- [X] Need login page `/accounts/login/`, registration page `/accounts/signup` styled to match other pages. (frontend?)

 
- [X] Comments on code (even a single sentence) for EVERYTHING from now on until submission!


- [X] Filter Events on browse

- [X] Commit/Uncommit to event

- [X] User shouldn't be able to commit to two events with overlapping date and time.

## From Requirements:

- [X] No: 1
Statement: The system shall allow for the log in /account creation of multiple users simultaneously
Evaluation Method: If a user enters the site and can either create an account or log into an account while a user does the same action

- [X] No: 2
Statement: The system display a list of sporting events that the user can create
Evaluation Method: If a user enters to create an session and there are multiple options for what sport is being played at the time of creation

- [X] No: 5
Statement: The system should have the ability to allow users to announce their attendance at an event 
Evaluation Method:A user should be able to access an event page and put their name down on the list of attendees

- [X] No: 6
Statement: The system should be able to support unique users
Evaluation Method: When a user creates an account they shouldn’t be able to create an account with the same email address or username

- [X] No: 4
Statement: The system should have the ability to provide a map overlay of the UCF campus and pinpoint event locations
Evaluation Method: Upon entering the website, a user should be able to see all of the locations that matches can be held and where specific events are being held

###### All we need is court locations and their sports

- [X] No: 7 -- Similar to 3
Statement: The system should allow for a user to check into an event
Evaluation Method:Once a user is at the event, they should be able to check in, confirming their attendence

###### For this, when someone commits, a check in button replaces it and is disabled until the event is only an hour away

- [X] No: 8
Statement: The system should have a point system rewarding members
Evaluation Method:A user should be given points for select actions like making an account, checking into games, etc.

###### Whenever a user checks in, or creates a game, a point is added to their reputation field

- [X] No: 9
Statement: The system will not allow a user to attend two events at once
Evaluation Method:The system will replace the old event with the new one or cancel the request to attend the new event 

###### Add this functionality to commit function

- [ ] No: 10
Statement: The system should allow the user to view other user’s history of games and points
Evaluation Method:A user should be able to click on a user’s name from an event page and have the information displayed

###### Add a function to the user controller that gets this data, and display it

## Extra Credit

- [ ] If a pickup game must be canceled on the day it's supposed to occur (i.e., due to weather, etc.), send a message to attendees' phones.
- [ ] Ability to add "friends" and invite them to specific events.

## Optional

- [ ] Comments on events.

- [X] Upload User image

 

Post issues (any issues) on Github




# Django GameServe
------------



## Python Environment Specification
-------------
1. You should use **virtualenv** to keep your python binary in your home directory (no more sudo). Run following from terminal
`virtualenv ~/.python`
`echo VIRTUAL_ENV_DISABLE_PROMPT=1 >> ~/.bash_profile`
`echo source $HOME/.python/bin/activate >> ~/.bash_profile`
`source ~/.bash_profile`

2. You should then use pip to install **django-extensions** so you can run custom scripts to fill db
`./manage.py runscript addDB`
`pip install django-extensions`
    - `runscript` allows python files located in scripts/ to run. Useful for scripts to add to DB etc


## DB Query
------------  
- All courts  
  `/api/v1/court/` 

- Next scheduled events after 7-18-2014 2:44AM  
  `/api/v1/event/?dateTime__gte=2014-7-18% 2:44`  

- Next schedules events on court id 1    
  `/api/v1/event/?dateTime__gte=2014-7-18 2:44&court=1`



## Notes
------------

1. Default Admin User account
    - Username: admin
    - Password: admin





>  Facebook DB entry  
-------------   
`./manage.py dbshell`  
```sql
UPDATE django_site SET DOMAIN = '127.0.0.1:8000', name = 'GameServe' WHERE id=1;
INSERT INTO socialaccount_socialapp (provider, name, secret, client_id, `key`)
VALUES ("facebook", "Facebook", "e42ec912bdf8d060d4e6c17ed4d294de", "650041485084650", '');
INSERT INTO socialaccount_socialapp_sites (socialapp_id, site_id) VALUES (1,1);
```
