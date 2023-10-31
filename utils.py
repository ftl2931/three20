#!/usr/bin/python3

import os

# Clear the log from past executions
def clear_log():
    os.system('truncate -s 0 ~/.three20.log')

# Append a message to the log
def log_msg(msg):
    # escape back slashes
    msg = msg.replace('\\', '\\\\')
    # and double quotes
    msg = msg.replace('"', '\\"')
    os.system(f'echo "{msg}" >> ~/.three20.log')

# Execute a command, read the output from a pipe and return it.
def popen_and_read(cmd, ignore_fail=True):
    pipe = os.popen(cmd)
    result = pipe.read().strip()
    exit_code = pipe.close()
    if exit_code is None or ignore_fail:
        return result
    else:
        print('the command failed with exit code: ', exit_code)
