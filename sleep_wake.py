#! python3

"""
sleep_wake.py

This program serves as an alarm.
It takes 4 inputs: sleep time in hours and minutes;
                   wake hour in hours and minutes

It will send a notification if the set time
is equivalent to the current time.
"""

from datetime import datetime
import pync

def ask_sleep_time():
    """
    workout(time, day) function

    This function asks for inputs
    """
    print("Note: Please enter with the 24 hour format and 2 digits only")
    while True: # asks at what hour does the user want to sleep
        sleep_hour = input("At what hour do you want to sleep?\n")
        if len(sleep_hour) != 2:
            print("Please enter 2 digits") # if the input isn't 2 digits, keep asking
        else:
            break

    while True: # asks at what minute does the user want to sleep
        sleep_minute = input("At what minute do you want to sleep?\n")
        if len(sleep_minute) != 2:
            print("Please enter 2 digts") # if the input isn't 2 digits, keep asking
        else:
            break

    while True: # asks at what hour does the user want to wake up
        wake_hour = input("At what hour do you want to wake up?\n")
        if len(wake_hour) != 2:
            print("Please enter 2 digits") # if the input isn't 2 digits, keep asking
        else:
            break

    while True: # asks at what minute does the user want to wake up
        wake_minute = input("At what minute do you want to wake up?\n")
        if len(wake_minute) != 2:
            print("Please enter 2 digits") # if the input isn't 2 digits, keep asking
        else:
            break

    return int(sleep_hour), int(sleep_minute), int(wake_hour), int(wake_minute)

def sleep_time_check():
    """
    sleep_time_check

    This function checks if the given
    schedule met the requirements which is
    7-9 hours of sleep.
    """
    minimum_req = 420 # 7 hours
    maximum_req = 540 # 9 hours
    sleep_hour, sleep_minute, wake_hour, wake_minute = ask_sleep_time()
    wake_hour = wake_hour + 24
    total_sleep_time = (wake_hour - sleep_hour)*60 + (wake_minute - sleep_minute) # calculate the total amount of sleep
    return total_sleep_time >= minimum_req and total_sleep_time <= maximum_req

def sleep_wake(current_time):
    """
    sleep

    This function pushes the notification
    if the given scheduled time is equivalent
    to the current time
    """
    while True:
        if sleep_time_check() is True:
            break
        print("Please set a sleeping schedule for 7-9 hours")
    sleep_hour, sleep_minute, wake_hour, wake_minute = ask_sleep_time()
    if f"{sleep_hour} {sleep_minute} 00" == current_time:
        pync.notify("Hey, it's time to sleep", title="Sleep Reminder")
    if f"{wake_hour} {wake_minute} 00" == current_time:
        pync.notify("Hey, it's time to wake up", title="Wake Up Reminder")


if __name__ == "__main__":
    curr_time = datetime.now()
    sleep_wake(curr_time.strftime("%H %M %S"))
