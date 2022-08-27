"""
vent.py

This program contains
"""

import json
import sys

def store(choice, message):
    with open("programming/python/data", "r") as fp:
        storage = json.load(fp)
    if choice.lower() == "yes":
        storage.append((message, "Anonymous"))
        with open("programming/python/data", "w") as fp:
            json.dump(storage, fp)
    else:
        name = input("\nType in your name to publish\n")
        storage.append((message, name))
        with open("programming/python/data", "w") as fp:
            json.dump(storage, fp)

def room():
    print("\n")
    with open("programming/python/data", "r") as fp:
        storage = json.load(fp)
    for i in range(len(storage)):
        print(f"""\n{storage[i][0]}

- {storage[i][1]}""")

def vent():
    """
    vent

    This function
    to be continued
    """
    print("Welcome! In this section you can just vent off as much as you like\n")
    text = []
    
    while True:
        line = input()
        if line:
            text.append(line)
        else:
            break

    message = "\n".join(text)
    print("""Do you want to publish this anonymously?
    
- Type 'yes' if you wish to publish this anonymously
- Type 'no' if you don't wish to publish this anonymously
    """)
    choice = input()
    store(choice, message)
    print("""\nDo you want to see the room section?
- Type 'yes' if you wish to.
- Type 'no' if you don't wish to.
    """)
    room_choice = input()
    if room_choice.lower() == "yes":
        room()
    else:
        sys.exit()
