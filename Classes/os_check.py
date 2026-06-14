from platform import system

class oscheck:
    
    def __init__(self):
        self.os = system()
    
    def checkos(self):
        return self.os
    