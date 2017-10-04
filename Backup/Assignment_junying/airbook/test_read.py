import csv

result_title = (
    'depature id', 'return id', 'departure date', 'return date', "promotional code", 'day diff', 'expected result',
    'actual result screen', "status")


def read_file(filename):
    with open(filename, 'r') as in_file, \
            open('test_output.csv', 'wb') as out_file:
        reader = csv.reader(in_file, delimiter=',', quotechar='"')
        writer = csv.writer(out_file, delimiter=',', quotechar='"')
        i = 0
        for row in reader:
            print row
            if i == 0:
                writer.writerow(result_title)
            else:
                depature_id, return_id, departure_date, return_date, promotional_code, day_diff, expected_result = row


                writer.writerow(row + ['abc', 'def'])
            i += 1


read_file('test_data.csv')
