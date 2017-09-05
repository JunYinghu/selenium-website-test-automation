class Leavecau(object): #this is new way to declare a class
#class Leavecau: #this is old way to declare a class
    def __init__(self):   # this is a class constructor with argument
        self.x=1

    def leaveanual(self,name,years):
        if years ==3:
            leaveanual = 18

        if years == 1:
            leaveanual = 12
        if years == 2:
            leaveanual = 15

        else:
            leaveanual = 10

        return (name,leaveanual)


    @classmethod
    def get_max_annual_leaave(cls):
        return 14

class TwoNumberOperation:
    @classmethod
    def add(cls, a, b):
        return a +b

    @classmethod
    def mult(cls, a, b):
        return a * b





