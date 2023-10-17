#!/usr/bin/python3

import os
import sys
import time
from datetime import datetime, timedelta
from utils import popen_and_read
from idle import get_idle_time, manage_idle_time

def issue_break():
    break_time = time.time()
    os.system('xmessage -center "Take a break"')
    delay = time.time() - break_time
    time.sleep(20)
    os.system('xmessage -center "Break over"')

mn = 60
break_interval = 20*mn

should_reset = True
should_stall = False

while True:
    if should_reset:
        break_time = time.time() + break_interval
        should_reset = False

    should_reset, should_stall = manage_idle_time(should_stall)

    if not should_reset:
        sleep_t = min(break_time - time.time(), 
                      2.1*mn - get_idle_time(), mn / 2)
        if sleep_t > 0: # if no prolonged idleness occurs, most of the execution time will be spent in this call
            # and this loop will run once every 30 seconds or so.
            time.sleep(sleep_t)
        if time.time() >= break_time:
            issue_break()
            should_stall = False
            should_reset = True

