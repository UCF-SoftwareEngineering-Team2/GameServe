from events.models import Sport, Court, Event
from profile.models import User
 
from allauth.account.models import EmailAddress
 
from django.db.utils import IntegrityError, ProgrammingError
from random import randint
import re
from __builtin__ import KeyboardInterrupt
from django.utils import timezone
 
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
 
 
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
    s = [
        'Basketball',
        'Football',
        'Tennis',
        'Volleyball',
        'Baseball',
        'Soccer',
        'Biking',
        'Running',
        'Ping-Pong',
        'RacquetBall'
    ]

    for i in s:
        try:
            sport = Sport()
            sport.sportType = i
            sport.save()
        except (IntegrityError):
            pass
 
 
def addEvents():
    print 'Adding Events ...'
    c = Court.objects.count()
    u = User.objects.count()
    s = Sport.objects.count()
 
 
    for i in range(5000):
        e = Event()
 
        year = 2014
        month = randint(1, 12)
        day = randint(1,30) if ( month != 2 ) else randint(1, 28)
 
        hour = randint(1, 23) - 2
        hour = 0 if (hour < 0) else hour
        minute = randint(0, 59)
 
        e.dateTime = timezone.datetime(year=year, month=month, day=day,
                                       hour=hour, minute=minute)
        e.endTime = timezone.datetime(year=year, month=month, day=day,
                                       hour=hour+2, minute=minute)
 
        e.court = Court.objects.get(id=randint(1,c))
        e.sport = Sport.objects.get(id=randint(1,s))
        e.creator  = User.objects.get(id=randint(2,u))
        e.duration = 2
        e.save()
        try:
            for i in range(randint(1,50)):
                e.participants.add(User.objects.get(id=randint(2,u)))
        except(User.DoesNotExist):
            pass
        e.save()
 
 
def addUsers():
    # from profile.models import User
    from profile.utils import create_allauth_user 
 
    print 'Adding users...'
    # Open file for read
    infile = open('.fakenames.txt','r')
    lines = infile.readlines()            # get all lines as list
 
    for line in lines:
 
        line = line.rstrip('\n')                            # remove newline+escapes
        line = filter(None, re.split('\s+',line))            # remove empty elements in list
 
        try:
            
            phone_number = line[3].replace('-','')
            phone_number = phone_number.rstrip('\n')

            
            u = create_allauth_user(email=line[1],
                                    username=line[2],
                                    password=line[2][::-1],
                                    phonenumber=phone_number)
            print HEADER+line[0]+ENDC
            print FAIL+"Email: "+u.email+ENDC
            print FAIL+"Username: "+u.username+ENDC
            # print FAIL+"Pass: "+u.password+ENDC
            print FAIL+"Phone: "+u.phone_number+ENDC
            print
 
        # If not unique
        except (IntegrityError, ProgrammingError):
            pass
 
 
 
 
def clearAllDB():
    Court.objects.all().delete()
    Sport.objects.all().delete()
    User.objects.all().delete()
    Event.objects.all().delete()
 
def printMenu():
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