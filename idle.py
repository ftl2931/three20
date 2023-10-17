#!/usr/bin/python3

## functions to manage idle time

import os
import time

from utils import popen_and_read

# The following identify programs which don't require frequent interaction, and consequently may cause reset prompts to appear
# even though you are still using the computer

# The first list identifies them by process name
holdoff_processes = ('evince', 'ebook-viewer')

# the second identifies them by strings included in the window title
holdoff_windows = ('VLC', )

def get_idle_time():
    xpi_output = popen_and_read('xprintidle')
    idle_time_ms = int(xpi_output)
    return idle_time_ms // 1000

def get_process_name(pid):
    ps_output = popen_and_read(f'ps -eo %p%c | grep {pid}')
    ps_entries = ps_output.split('\n')

    for e in ps_entries:
        entry_info = e.split(' ')
        if entry_info[0] == str(pid):
            return entry_info[1]

def get_active_window_info():
    window_name = popen_and_read('xdotool getactivewindow getwindowname', False)
    window_pid = popen_and_read('xdotool getactivewindow getwindowpid', False)
    process_name = get_process_name(window_pid)
    return window_name, process_name

def should_holdoff_idle():
    active_window_name, active_window_pid = get_active_window_info()
    active_window_proc_name = get_process_name(active_window_pid)
    if active_window_name is None:
        print('Failed to get the pid of the process that owns the current active window. You should use a window title if possible.')
    if active_window_proc_name in holdoff_processes:
        return True
    for name in holdoff_windows:
        if name in active_window_name:
            return True
    return False
     
def manage_idle_time(stall):
    should_reset = should_stall = False
    idle_time = get_idle_time()
    holdoff_idle = should_holdoff_idle()
    if not (stall or holdoff_idle) and idle_time >= 2 * 60:
        start_time = time.time()
        choice = os.system('xmessage -buttons reset:0,stall:2 -center "Idle..."') >> 8
        # when closing the window without choosing an option, xmessage returns 1
        # Since this is relatively faster to do with a keyboard, it is associated with the 'ignore' action
        if choice == 0:
            should_reset = True
        elif choice == 2: 
            should_stall = True
    if stall:
        should_stall = True
    return should_reset, should_stall




