import datetime
import time


def form_date(year, month, day):
    month = str(month)
    if len(month) == 1:
        month = "0" + month
    day = str(day)
    if len(day) == 1:
        day = "0" + day
    return str(year) + "-" + str(month) + "-" + str(day)


def check_date(year, month, day):
    try:
        # print year,month,day
        time.strptime(form_date(year, month, day), "%Y-%m-%d")
        # print "Accepted"
        return True
    except Exception as e:
        # print e
        return False


def create_error(msg):
    return {"code": 1, "msg": msg}


def create_success(msg):
    return {"code": 0, "msg": msg}


def print_time():
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
