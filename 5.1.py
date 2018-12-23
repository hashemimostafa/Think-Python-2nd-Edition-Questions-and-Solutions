# =============================================================================
# The time module provides a function, also named time, that returns 
# the current Greenwich Mean Time in “the epoch”, which is an arbitrary time
# used as a reference point. On UNIX systems, the epoch is 1 January 1970.
# >>> import time
# >>> time.time()
# 1437746094.5735958
# Write a script that reads the current time and converts it to a time of day
# in hours, minutes, and seconds, plus the number of days since the epoch.
# =============================================================================

import time
now = time.time()

m = 60
h = 3600
d = 86400
yr = 86400 * 365

_days = now // d
_hours = (now - _days * d) // h
_minutes = (now - _days * d - _hours * h) // m
_seconds = now - _days * d - _hours * h - _minutes * m
print(int(_days), 'days, ', int(_hours), 'hours, ', int(_minutes), 'minutes, ',
      int(_seconds), 'seconds \nafter the Epoch time.\n')

year = 1970 + now // yr
now -= (year -1970) * yr
month = now // d

if month <= 31:
    name_month = 'Jan'
    day = now // d
elif month <= 59:
    name_month = 'Feb'
    day = now // d -  31
elif month <= 90:
    name_month = 'Mar'
    day = now // d - 59
elif month <= 120:
    name_month = 'Apr'
    day = now // d - 90
elif month <= 151:
    name_month = 'May'
    day = now // d - 120
elif month <= 181:
    name_month = 'Jun'
    day = now // d - 151
elif month <= 212:
    name_month = 'July'
    day = now // d - 181
elif month <= 243:
    name_month = 'Aug'
    day = now // d - 212
elif month <= 273:
    name_month = 'Sep'
    day = now // d - 243
elif month <= 304:
    name_month = 'Oct'
    day = now // d - 273
elif month <= 334:
    name_month = 'Nov'
    day = (now // d) - 304
elif month <= 365:
    name_month = 'Dec'
    day = now // d - 334

# Ignored from leap years or seconds
print('Approximately ~', int(day), name_month, int(year))