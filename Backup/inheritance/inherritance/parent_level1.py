class Creature(object):
    def __init__(self,name):
        self.name = name

    def grow(self):
       print self.name,'grow'