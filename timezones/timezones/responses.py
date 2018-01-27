
import json
from flask import Response

from utils import dt_to_dict

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


def invalid_user_input():
    content = {"error": "Invalid User Input"}

    return Response(json.dumps(content),
                    mimetype="application/json",
                    status="400")


def add_watchlist_resp(location, dt, timezone):
    content = location
    content["timezone"] = timezone["timeZoneName"]
    content["timezoneid"] = timezone["timeZoneId"]
    content["utcoffset"] = timezone["rawOffset"]
    content["datetime"] = dt_to_dict(dt)

    return content
