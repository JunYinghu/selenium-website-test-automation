import calendar
from datetime import date
from datetime import datetime
from datetime import timedelta

file = "testing"

# format datetime
def caludate():
    now = datetime.now()
    print now.strftime("%Y")
    print now.strftime("%y")
    print now.strftime("%a,%d,%B,%y")
    print now.strftime("%c")
    print now.strftime("%x")
    print now.strftime("%X")
    print now.strftime("%I,%M,%S,%p")
    print now.strftime("%H,%M")

caludate()

# Print calendar
for m in range(1, 13):
    cal =calendar.monthcalendar(2017, m)
    #if the first firday has be within the first two weeks
    weekone = cal[0]
    weektwo = cal[1]
    # if the first firday not in week 1 it must be in week 2
    if weekone [calendar.FRIDAY] !=0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo [calendar.FRIDAY]
    print "%10s %2d" % (calendar.month_name[m],meetday)

for name in calendar.month_name:
    print name

for day in calendar.day_name:
    print day

hc = calendar.TextCalendar(calendar.MONDAY)
calstr = hc.formatmonth(2017, 9, 0, 0)

print calstr

hchtml = calendar.HTMLCalendar(calendar.SUNDAY)
strcalhtml = hc.formatmonth(2017, 9)
print strcalhtml

for i in calendar.c.itermonthdays(2013, 9):
    print i


# hc = calendar.LocaleHTMLCalendar(calendar.MONDAY)
# str = hc.formatmonth(2017,1)

# Timedeltas

def datetimecau():
    print timedelta(days=365, hours=5, minutes=3)
    print str(datetime.now())
    print 'next 356 days ' + str(datetime.now() + timedelta(days=365))
    print 'next 5 houws ' + str(datetime.now() + timedelta(hours=5))
    a = datetime.now() + timedelta(days=-5)
    print '5 days ago ', a.strftime("%A, %B, %d, %Y")
    today = date.today()
    afd = date(today.year, 4, 1)
    if afd < today:
        print "april fools day already went by %d days agao" % ((today - afd).days)
        afd = afd.replace(year=today.year + 1)
        print  "afd ddddd", afd
        time_to_afd = abs(afd - today)
        print time_to_afd, "days until next april fools day!"
datetimecau()



def gamce():
    # x = raw_input()
    # (i,j) = map(int,raw_input().split( ))
    #   print x
    # print 'ddd'
    pass

def gettextglobel():
    print 'ddddd {}', file

gettextglobel()
print gettextglobel()
print gettextglobel

def fun1(*arg1):
    result = 0
    x = 3
    for i, d in enumerate(arg1):
        if i == 1: continue
        result = result + d * x
        index = i
        print index, d
        # print x
    # print ("jlsjdfa"), arg1 + x
    return result


print fun1(1, 2, 3, 4, 5)


def caul(x, y):
    if x > y:
        st = ' x is morethan y'
    elif x == y:
        st = 'x is = y'
    else:
        st = 'x is less than y'
    return st


print caul(4, 4)


def fileexu():
   # f = open("textfile.txt","w++")
    f = open("textfile.txt", "a+")
    for i in range (10):
        f.write("this is line %d\r\n" %(i+1))
        f.close()
fileexu()
if __name__ == '__main__':
    gamce()
