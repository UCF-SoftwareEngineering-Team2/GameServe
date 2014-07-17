import os
from events.models import Sport, Court, Event
# from django.contrib.auth.models import User
from accounts.models import User
from django.db.utils import IntegrityError, ProgrammingError
from random import randint
import datetime
import re
from __builtin__ import KeyboardInterrupt
from django.utils import timezone

def addCourts():
    print 'Adding Courts'
    c =[(28.596449, -81.201287),(28.595977, -81.197659),(28.596067, -81.197476),(28.596082, -81.197285),
        (28.596148, -81.197116),(28.595687, -81.197641),(28.595688, -81.197422),(28.595742, -81.197258),(28.595754, -81.197081),(28.607421, -81.196185),(28.594833, -81.200847),
        (28.594857, -81.200703),(28.594814, -81.200532),(28.596039, -81.197903)]
    s = len(Sport.objects.all())
    if s < 2:
        addSports()
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
    from accounts.models import User
    print 'Adding Events ...'
    c = len(Court.objects.all())
    u = len(User.objects.all())
    today = datetime.date.today()
    for i in range(5000):
        e = Event()
        e.dateTime = timezone.datetime(year=2014, month=randint(1,12), day=randint(1,28),
                                       hour=randint(0,23), minute=randint(0,59))


        e.court = Court.objects.get(id=randint(1,c))


        try:
            e.creator = User.objects.get(id=randint(1,u))
            e.save()
        except(User.DoesNotExist):
            continue
        try:
            for i in range(50):
                e.participants.add(User.objects.get(id=randint(1,u)))
        except(User.DoesNotExist):
            pass

        e.save()


def addUsers():
    from accounts.models import User
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    print 'Adding users...'
    # Open file for read
    infile = open('.fakenames.txt','r')
    lines = infile.readlines()            # get all lines as list

    for line in lines:
        userr = User()

        line = line.rstrip('\n')                            # remove newline+escapes
        line = filter(None, re.split('\s+',line))            # remove empty elements in list

        try:
            userr.first_name = line[0]
            print HEADER+userr.first_name+ENDC

            userr.email = line[1]
            print FAIL+userr.email+ENDC

            userr.username = line[2]
            print FAIL+userr.username+ENDC

            tmp = line[2]
            userr.password = tmp[::-1]
            print FAIL+userr.password+ENDC
            print
            # profile = UserProfile( phone_number = line[3].replace('-','') )
            # profile.user = userr
            # userr.save()
            # userr.profile = profile
            # profile.save()
            userr.phone_number = line[3].replace('-','')
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
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    print '---------------'
    print HEADER+'Menu'+ENDC
    print '---------------'
    print FAIL+'1. addSports()'+ENDC
    print FAIL+'2. addUsers()'+ENDC
    print FAIL+'3. addCourts()'+ENDC
    print FAIL+'4. addEvents()'+ENDC
    print FAIL+'5. Add All'+ENDC
    print FAIL+'6. ClearAllDB()'+ENDC
    print WARNING+'*. Exit'+ENDC
    print

def run():
    try:
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
        elif choice == 6:
            clearAllDB()
        else:
            return
    except ( KeyboardInterrupt ):
        run()

