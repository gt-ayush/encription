import random
import hashlib
import time
from utils.time_utils import get_timestamp, get_timezone_offset

def generate_key():
    timestamp = get_timestamp()
    tz_offset = get_timezone_offset()
    
    delay = random.randint(1, 9999)
    time.sleep(0.001)

    raw = timestamp + tz_offset + str(delay)
    return hashlib.sha256(raw.encode()).digest()

