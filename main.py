from command import Command
from hook import HOOK
from dynaimport import discover_and_import_modules

def funcontick():
    print("YOOO")

commands = [Command("function", funcontick)]

discover_and_import_modules('Mods', commands)

user_input = input("Enter the command name: ")

for command in commands:
    if command.name == user_input:
        command.callontick()  
        break
else:
    print("Command not found")
