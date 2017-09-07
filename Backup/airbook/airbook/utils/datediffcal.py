from datetime import datetime


def date_covert(current_depature_id, current_return_id):
    depature_date_dict = {1: '2017-7', 2: '2017-12', 3: '2018-7', 4: '2018-12', 5: "2019-7", 6: "2019-12"}
    return_date_dict = {1: '2017-7', 2: '2017-12', 3: '2018-7', 4: '2018-12', 5: "2019-7", 6: "2019-12"}
    depature_date = depature_date_dict.get(current_depature_id, "")
    return_date = depature_date_dict.get(current_return_id, "")
    return depature_date, return_date


def day_diff_cal(current_depature_id, current_return_id):
    if current_depature_id == 0 or current_return_id == 0:

        return 0
    else:
        (depature_date, return_date) = date_covert(current_depature_id, current_return_id)
        # print ("+++++++++++++++++this is depature_date, return_date+++++++++++++++++++"), depature_date, return_date
        x1 = datetime.strptime(depature_date, "%Y-%m")
        x2 = datetime.strptime(return_date, "%Y-%m")
        diff = x2 - x1
        # print ("++++++this is diff days between departure and return+++++++++"), diff.days
        return diff.days
