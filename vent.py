"""
vent.py

This program takes a multiline
string as an input. Then, it'll
ask whether the user will publish
the given string anonymously or not.
Also, it'll ask whether the user
wants to see other's message.
"""

import os
import json
import sys

def store(choice, message):
    """
    store

    This function opens a file and stores
    it to a variable. The function will
    append the message and rewrites the data.
    """
    with open("programming/python/data", "r") as fp:
        storage = json.load(fp) # transfers file data to the variable
    if choice.lower() == "yes":
        storage.append((message, "Anonymous"))
        with open("programming/python/data", "w") as fp:
            json.dump(storage, fp) # rewrites data
    else:
        name = input("\nType in your name to publish\n") # asks for name
        storage.append((message, name))
        with open("programming/python/data", "w") as fp:
            json.dump(storage, fp) # rewrites data

def room():
    """
    room

    This function displays
    all of the messages that has
    been stored in the data
    """
    os.system("clear")
    with open("programming/python/data", "r") as fp:
        storage = json.load(fp) # reads data
    for i in range(len(storage)):
        print(f"""\n{storage[i][0]}

- {storage[i][1]}""") # displays message then name

def vent():
    """
    vent

    This function takes a multiline
    string and asks the user whether
    it wants to publish it anonymously
    or not. It also asks whetehr the user
    wants to see other messages as well.
    """
    print("Welcome! In this section you can just vent off as much as you like\n")
    text = []
    
    while True: # multiline input
        line = input()
        if line:
            text.append(line)
        else:
            break

    message = "\n".join(text) # joins it into a single string
    print("""Do you want to publish this anonymously?
    
- Type 'yes' if you wish to publish this anonymously
- Type 'no' if you don't wish to publish this anonymously
    """)
    choice = input()
    store(choice, message) # stores data
    print("""\nDo you want to see the room section?
- Type 'yes' if you wish to.
- Type 'no' if you don't wish to.
    """)
    room_choice = input()
    if room_choice.lower() == "yes":
        room() # shows all messages
    else:
        sys.exit() # exits
