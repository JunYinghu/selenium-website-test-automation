import os
from datetime import datetime
from time import time

globlevar = "testing globle var"

#os.remove('/tmp/aaaaa.txt')
DEFAULT_FACTOR = 1.0

class AWS(object):
    def __init__(self):
        pass


class PerformanceBonus(object):
    def __init__(self, base_sallary):  # constructor
        self.base_sallary = base_sallary

    def min_bonus(self, factor, kpi=0):
        def calculate(a, b):
            return a * b

        if factor > 10000:

            return calculate(self.base_sallary, factor) + kpi
        else:
            return 0

    def get_time(self):
        return int(time())

    def get_date(self):
        return datetime.today()

    def get_date_diff(self, (y1, m1, d1), (y2, m2, d2)):
        x1 = datetime(y1, m1, d1)
        x2 = datetime(y2, m2, d2)
        diff = x1 - x2
        return diff.days

    def get_date_diff_str(self, format, s1, s2):
        x1 = datetime.strptime(s1, format)
        x2 = datetime.strptime(s2, format)
        diff = x1 - x2
        return diff.days

    def format_date_diff_str(self, format, s1, s2):
        x1 = datetime.strptime(s1, format)
        x2 = datetime.strptime(s2, format)
        diff = x1 - x2
        return str(diff)
