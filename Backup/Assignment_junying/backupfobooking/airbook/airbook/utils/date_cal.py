from datetime import datetime


def datecovert(d, r):
    depature_date_dict = {1: '2017-7', 2: '2017-12', 3: '2018-7', 4: '2018-12', 5: "2019-7", 6: "2019-12"}
    return_date_dict = {1: '2017-7', 2: '2017-12', 3: '2018-7', 4: '2018-12', 5: "2019-7", 6: "2019-12"}
    depature_date = depature_date_dict.get(d, "")
    return_date = depature_date_dict.get(r, "")
    return (depature_date, return_date)


def datecau(d, r):
    if d == 0 or r == 0:
        # print ("++++++++++++++++this is for date cau+++++++++++++"), d, r
        # status = "failed"
        # expected_result = "Unfortunately, this schedule is not possible. Please try again."
        # print expected_result
        return 0
    else:
        (depature_date, return_date) = datecovert(d, r)
        # print ("+++++++++++++++++this is depature_date, return_date+++++++++++++++++++"), depature_date, return_date
        x1 = datetime.strptime(depature_date, "%Y-%m")
        x2 = datetime.strptime(return_date, "%Y-%m")
        diff = x2 - x1
        #print ("++++++this is diff days between departure and return+++++++++"), diff.days
        return diff.days
