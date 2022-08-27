"""
workout.py

This program ...
"""

from plyer import notification

def ask_workout_time():
    """
    ask_sleep_time

    This function asks for inputs
    """
    while True:
        ask_hour = input("At what hour do you want to start your workout?\n")
        if len(ask_hour) != 2:
            print("Please enter 2 digits")
        break

    while True:
        ask_minute = input("At what minute do you want to start your workout?\n")
        if len(ask_minute) != 2:
            print("Please enter 2 digits")
        break

    while True:
        ask_duration = input("How long do you want your workout to last? (minutes)\n")
        if len(ask_duration) == 0:
            print("Please enter a valid duration")
        break

    return ask_hour, int(ask_minute), int(ask_duration)

def workout(start_hour, start_minute, _duration, current_time):
    """
    workout

    This function
    """
    if f"{start_hour} {start_minute} 00" == current_time:
        notification.notify(
            title="Workout Reminder",
            message="Hey, it's time for your workout",
            timeout=10
            )
    end_hour = int(start_hour)
    end_minute = start_minute + _duration
    if end_minute >= 60:
        end_hour += (end_minute//60)
        end_minute -= 60
    if end_hour < 10:
        end_hour = f"0{end_hour}"
    if f"{end_hour} {end_minute} 00" == current_time:
        notification.notify(
            title="Workout Reminder",
            message="Hooray! You've just reached your goal!",
            timeout=10
            )
        return True

