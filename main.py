"""
main.py


"""
import time
from datetime import datetime
import sleep_wake as s
import workout as w
import vent as v

if __name__ == "__main__":
    print("Well, hello there!")
    time.sleep(3)
    function = input("""\nWhich function do you want to use?
    
- Type 'sleep' to access the sleep and wake alarm
- Type 'workout' to access the workout timer
- Type 'vent' to vent out
    \n""")
    if function.lower() == "sleep":
        print("Initialising...")
        time.sleep(2)
        print("Please enter with the 24 hour format and 2 digits only")
        while True:
            sleep_hour, sleep_minute, wake_hour, wake_minute = s.ask_sleep_time()
            if s.sleep_time_check(sleep_hour, sleep_minute, wake_hour, wake_minute) is True:
                break
            print("Please enter a sleep schedule between 7-9 hours")
        while True:
            curr_time = datetime.now()
            s.sleep_wake(sleep_hour, sleep_minute, wake_hour, wake_minute, curr_time.strftime("%H %M %S"))
            time.sleep(1)
    elif function.lower() == "workout":
        print("Initialising...")
        time.sleep(2)
        hour, minute, duration = w.ask_workout_time()
        while True:
            now = datetime.now()
            if w.workout(hour, minute, duration, now.strftime("%H %M %S")) is True:
                break
            time.sleep(1)
    elif function.lower() == "vent":
        print("Initialising...")
        v.vent()
