import time
import datetime

def get_timestamp():
    return str(int(time.time()))

def get_timezone_offset():
    tz_offset = datetime.datetime.now().astimezone().utcoffset()
    return str(int(tz_offset.total_seconds()))

