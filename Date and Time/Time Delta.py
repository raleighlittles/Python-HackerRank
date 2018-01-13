#!/bin/python3

import sys, datetime, calendar

def time_delta(t1, t2):
    # Complete this function
    from datetime import datetime
    seconds_difference = int(abs((t2-t1).total_seconds()))
    return seconds_difference

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        t1=datetime.datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
        t2=datetime.datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
        delta = time_delta(t1, t2)
        print(delta)
