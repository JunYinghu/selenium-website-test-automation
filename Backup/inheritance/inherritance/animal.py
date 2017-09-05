from parent_level1 import Creature

class Animal (Creature):
    def __init__(self,name):
        Creature.__init__(self, name)

    def eat(self):
        print self.name, 'eat'



class Insect (Animal):
    def climb(self):
        print 'climb'

class Brid (Animal):
    def fly(self):
        print 'fly'

class Fish (Animal):
    def __init__(self,name):
        Animal.__init__(self,name)

    def swim(self):
        print self.name,"swim"


class Ant (Insect):

     def climb (self):
         print 'ant climb'

class Chicken(Brid):
    def fly (self):
        print 'chicken fly'

class Shark (Fish):
    def __init__(self,name):
        Fish.__init__(self,name)
    def swim(self):
        print self.name, "shart swim"

