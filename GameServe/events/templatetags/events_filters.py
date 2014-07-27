import time
from django import template

register = template.Library()

# Filter that takes in a datetime value, and turns it into a UTC Timestamp, allows us to
# query for a certain event time by URL
def getTimeStamp(value):
	return int(time.mktime(value.timetuple()))

register.filter('getTimeStamp', getTimeStamp)