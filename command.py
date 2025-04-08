# command.py

class Command:
    def __init__(self, name, ontick):
        self.name = name
        self.ontick = ontick

    def callontick(self):  
        self.ontick()
