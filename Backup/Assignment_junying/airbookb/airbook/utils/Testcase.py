import re
def prom_verify(input_prom_cod):
    # print "here" + prom_cod
    if re.match('[A-Z]{2}[1-9]-?[A-Z]{3}-?[0-9]{3}', input_prom_cod):
        # print "here2"
        digit_1 = input_prom_cod[2]
        digit_2 = input_prom_cod[8]
        digit_3 = input_prom_cod[9]
        digit_4 = input_prom_cod[10]
        digit_sum = int(digit_1) + int(digit_2) + int(digit_3)
        print digit_sum
        if int(digit_4) == (digit_sum % 10):
            # print "Here"
            return True
    return False


