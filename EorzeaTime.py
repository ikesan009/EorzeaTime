#coding: utf-8
import datetime
import time


def main():
    dict_week = {
        "Sunday":0,
        "Monday":1,
        "Tuesday":2,
        "Wednesday":3,
        "Thursday":4,
        "Friday":5,
        "Saturday":6
        }

    while True:
        date_now = datetime.datetime.now()
        date_sunday = date_now - datetime.timedelta(days=dict_week[date_now.strftime('%A')])
        date_sunday = datetime.datetime(date_sunday.year, date_sunday.month, date_sunday.day, 0, 0, 0, 0)
        date_difference = date_now - date_sunday
        seconds_difference = date_difference.total_seconds()
        seconds_eorzea = seconds_difference * 3600 / 175
        date_eorzea = datetime.timedelta(seconds=seconds_eorzea)
        minutes = date_eorzea.seconds / 60
        hours, minutes = divmod(minutes, 60)
        print("\rET: "+"{:02}".format(int(hours))+":"+"{:02}".format((int(minutes))), end="")
        time.sleep(2.9)


if __name__ == "__main__":
    main()