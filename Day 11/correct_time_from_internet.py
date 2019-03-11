# Only Administrator can change date and time.

import win32api
from _datetime import datetime, timedelta
from urllib.request import urlopen
import time

def set_time(time_tuple):
    dayOfWeek = datetime(*time_tuple).isocalendar()[2]
    t = time_tuple[:2] + (dayOfWeek,) + time_tuple[2:]
    win32api.SetSystemTime(*t)
    return True

result = (urlopen('http://just-the-time.appspot.com/').read().strip()).decode('utf-8')
NepalCurrentTime=datetime.strptime(result, '%Y-%m-%d %H:%M:%S')
NepalCurrentTime =  tuple(map(int,datetime.strftime(NepalCurrentTime, "%Y,%m,%d,%I,%M,%S,0").split(',')))
if set_time(NepalCurrentTime):
    print("Successfully changed date and time.")
    time.sleep(2)