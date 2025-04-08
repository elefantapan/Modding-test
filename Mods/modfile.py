from command import Command
from hook import HOOK

def countontick():
    print(11)

def foodontick():
    print(21)

# Create the 'count' and 'food' commands
count = Command("count", countontick)
food = Command("food", foodontick)

def mymod():
    print("Thisismycode - Hooked into 'callontick'")

# Hook into the `callontick` method of all Command instances
HOOK("callontick", mymod, position="after")

# Define the `commands` list that will be dynamically loaded into `main.py`
commands = [count, food]
