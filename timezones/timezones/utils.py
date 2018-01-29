import os

months = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"
         }

days = {
           0: "Monday",
           1: "Tuesday",
           2: "Wednesday",
           3: "Thursday",
           4: "Friday",
           5: "Saturday",
           6: "Sunday",

       }


def root_dir():
    return os.path.abspath(os.path.dirname(__file__))


def get_file(filename):
    try:
        src = os.path.join(root_dir(), filename)
        return open(src).read()
    except IOError as e:
        return str(e)

def dt_to_dict(dt):
    return {
               "year": dt.year,
               "month":  months[dt.month],
               "day": dt.day,
               "hour": "{:02d}".format(dt.hour),
               "minute": "{:02d}".format(dt.minute),
               "second": "{:02d}".format(dt.second),
               "weekday": days[dt.weekday()]
           }
