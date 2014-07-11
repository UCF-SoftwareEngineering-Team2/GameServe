import os
from events.models import Sport, Court, Event
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from random import randint
import datetime
import re
from django.db.utils import ProgrammingError

def addCourts():
    print 'Adding Courts'
    c =[(28.596449, -81.201287),(28.595977, -81.197659),(28.596067, -81.197476),(28.596082, -81.197285),
        (28.596148, -81.197116),(28.595687, -81.197641),(28.595688, -81.197422),(28.595742, -81.197258),(28.595754, -81.197081),(28.607421, -81.196185),(28.594833, -81.200847),
        (28.594857, -81.200703),(28.594814, -81.200532),(28.596039, -81.197903)]
    s = len(Sport.objects.all())

    for i in c:
        court = Court()
        court.sport = Sport.objects.get(id=randint(1,s))
        court.latitude, court.longitude = i
        court.save()

def addSports():
    print 'Adding sports'
    s = ['Basketball','Football','Tennis','Golf','Hockey','Swimming','Baseball','Soccer','Biking','Running','Shooting','Putting']
    for i in s:
        try:
            sport = Sport()
            sport.sportType = i
            sport.save()
        except (IntegrityError):
            pass


def addEvents():
    print 'Adding Events ...'
    c = len(Court.objects.all())
    u = len(User.objects.all())
    today = datetime.date.today()
    for i in range(5000):
        e = Event()
        e.date = datetime.date(2014,randint(today.month,12),randint(today.day,30))
        e.time = datetime.time(randint(0,23),randint(0,59))
        e.court = Court.objects.get(id=randint(1,c))
        e.creator = User.objects.get(id=randint(1,u))
        e.save()
        for i in range(50):
            e.users.add(User.objects.get(id=randint(1,u)))
        e.save()


def addUsers():
    print 'Adding users...'
    # Open file for read
    infile = open('.fakenames.txt','r')
    lines = infile.readlines()            # get all lines as list

    for line in lines:
        userr = User()

        line = line.rstrip('\n').replace('\xef\xbb\xbf','')  # remove newline+escapes
        line = filter(None, re.split('\s+',line))            # remove empty elements in list

        try:
            userr.first_name = line[0]
            print userr.first_name
            userr.email = line[1]
            print userr.email
            userr.username = line[2]
            print userr.username
            tmp = line[2]
            userr.password = tmp[::-1]
            print userr.password
            userr.save()
        # If not unique
        except (IntegrityError, ProgrammingError):
            pass





def clearAllDB():
    Court.objects.all().delete()
    Sport.objects.all().delete()
    User.objects.all().delete()
    Events.objects.all().delete()

def printMenu():
    print '---------------'
    print 'Menu'
    print '---------------'
    print '1. addSports()'
    print '2. addUsers()'
    print '3. addCourts()'
    print '4. addEvents()'
    print '5. All'
    print '*. Exit'
    print

def run():
    printMenu()
    choice = int(raw_input('Enter Choice: '))
    if choice == 1:
        addSports()
    elif choice == 2:
        addUsers()
    elif choice == 3:
        addCourts()
    elif choice == 4:
        addEvents()
    elif choice == 5:
        addSports()
        addUsers()
        addCourts()
        addEvents()
    else:
        return


