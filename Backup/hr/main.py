from hr import VERSION   # a way to import var from _init_.py
from hr.types.bonus import globlevar   # a way to import a globle var from a.py file

from hr.leave.leavecau import Leavecau, \
    TwoNumberOperation  # a way to import class without __init__ (contractor) from a.py file
# a way to import class with classmethod from a.py file

from hr.types.bonus import AWS
from hr.types.bonus import PerformanceBonus # a way to import a class with _init_ from a.py file

from hr.payroll import calculate_tax # a way to import function from _init_.py

from hr.types.bonus import DEFAULT_FACTOR

from hr.payroll.payrollcal import payrollcal # a way to import function from _init_.py


#Can print and using everywhere
print "this is from outside of fun/class" ,VERSION # Using a way to import var from _init_.py and use it in a function
print "this is from outside of fun/class" ,globlevar # Using a way to import a globle var from a.py file
#VERSION = '2.0.0'

def useing(): # using a way to import class without __init__ (contractor) from a.py file
    leavecau = Leavecau()
    print leavecau.leaveanual("wanghong", 3)

    # using a way to import a class with _init_ from a.py file
    x = PerformanceBonus(1000)
    print x.min_bonus(1.0, 0)
    print calculate_tax(1000) #using a way to import function from _init_.py
    return TwoNumberOperation.add(1,2) #using a way to import class with classmethod from a.py file

class MyClass(object):
    print "This is from class", VERSION  # Using a way to import var from _init_.py and use it in a function
    print "This is from class",globlevar  # Using a way to import a globle var from a.py file

    # a way to import class without __init__ (contractor) from a.py file, the condition is the imported class does not
    # have constructor or the constructor does not have arguement.
    leavecau1 = Leavecau()
    base_sallary= 1000

    def __init__(self,base_sallary=0): # using a way to import class without __init__ (contractor) from a.py file
        #self.base_sallary = base_sallary
        self.leavecau = Leavecau()
        self.performancebounus = PerformanceBonus(self.base_sallary)

    def test(self):
        print self.leavecau.leaveanual("wangli",2)
        print self.leavecau1.leaveanual("liping",1)
        print self.performancebounus.min_bonus(1.0, 0)
        print calculate_tax(1000)
        print TwoNumberOperation.add(100,20)  #using a way to import class with classmethod from a.py file
        print Leavecau.get_max_annual_leaave()#using a way to import class with classmethod from a.py file

print "this is from fun, outside class", useing()

# class RecordStudy():
#
#     def main(self):
#         Leavecau
#
#         print VERSION # a way to import var from _init_.py and use it in a function
#         print globlevar # a way to inport a globle var from a.py file
#         print calculate_tax(1000)
#
#         pb = PerformanceBonus(5000)
#         print pb.min_bonus(0.2, 120)
#         print pb.get_time()
#         print pb.get_date()
#         # print pb.get_date_diff((2017, 9, 30), (2018, 8, 1))
#         start_date = "2017-08"
#         print ("hell: "),pb.get_date_diff_str("%Y-%m", start_date, "2017-01")
#         #print pb.format_date_diff_str("%Y-%m-%d", start_date, "2017-01-01")

if __name__ == '__main__':
    a=MyClass()
    a.test()