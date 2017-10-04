import random
import string
from random import randint


def promcodgent():
    prom_cod = ''
    prom_cod_arr = []
    letter_1 = random.choice(string.ascii_letters)
    prom_cod_arr.append(letter_1)
    letter_2 = random.choice(string.ascii_letters)
    prom_cod_arr.append(letter_2)
    prom_cod_arr.append("-")
    letter_3 = random.choice(string.ascii_letters)
    prom_cod_arr.append(letter_3)
    letter_4 = random.choice(string.ascii_letters)
    prom_cod_arr.append(letter_4)
    letter_5 = random.choice(string.ascii_letters)
    prom_cod_arr.append(letter_5)
    prom_cod_arr.append("-")
    digit_1 = randint(0, 9)
    digit_2 = randint(0, 9)
    digit_3 = randint(0, 9)
    # print ("There are digit :"), digit_1, digit_2, digit_3
    if digit_1 + digit_2 + digit_3 < 10:
        digit_4 = digit_1 + digit_2 + digit_3
        # print digit_4
    else:
        t = digit_1 + digit_2 + digit_3
        digit_4 = (t % 10)
        # (abs(t) % (10 ** 1)) / (10 ** (1 - 1))
        # print ("______digit_4"), digit_4
    digit_1 = str(digit_1)
    prom_cod_arr.insert(2, digit_1)
    digit_2 = str(digit_2)
    prom_cod_arr.insert(10, digit_2)
    digit_3 = str(digit_3)
    prom_cod_arr.insert(11, digit_3)
    digit_4 = str(digit_4)
    prom_cod_arr.append(digit_4)
    # print ("this are digit :"), digit_1, digit_2, digit_3,digit_4
    pro_cod = ''.join(prom_cod_arr)
    pro_cod = str.upper(pro_cod)
    print ("This is final code:"), pro_cod
    return (pro_cod)


def promcodgentinvalid():
    # prom_codinvalid = ''
    chars = string.letters + string.digits + string.punctuation
    i = [1, 30]
    size = random.choice(i)
    prom_codinvalid = ''.join([random.choice(chars) for x in xrange(size)])

    return (prom_codinvalid)


import re


# import sys


# this function validates promo code and returns boolean
def promverify(prom_cod):
    # print "here" + prom_cod
    if re.match('[A-Z]{2}[1-9]-?[A-Z]{3}-?[0-9]{3}', prom_cod):
        # print "here2"
        digit_1 = prom_cod[2]
        digit_2 = prom_cod[8]
        digit_3 = prom_cod[9]
        digit_4 = prom_cod[10]
        digit_sum = int(digit_1) + int(digit_2) + int(digit_3)
        print digit_sum
        if int(digit_4) == (digit_sum % 10):
            # print "Here"
            return True
    return False
