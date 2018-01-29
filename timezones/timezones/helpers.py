
import requests

from datetime import datetime, timedelta

from timezones import utils
from timezones.exceptions import ServiceFailed

TIMEZONE_URL = "https://maps.googleapis.com/maps/api/timezone/json?location={lat},{lon}&timestamp={timestamp}&key=AIzaSyBT92tKXjQUXigZPUy1cGYGceRkaUekT4A"

def fetch_timezone(lat, lon, timestamp, **kwargs):

    url = TIMEZONE_URL.format(lat=lat, lon=lon, timestamp=timestamp)
    resp = requests.get(url)
    try:
        content = resp.json()
    except Exception:
        raise ServiceFailed("Invalid Response")

    if "status" not in content and content["status"] != "OK":

        raise ServiceFailed("Invalid Response")

    return content

def new_utc(utc_offset):

    offset = timedelta(seconds=utc_offset)

    return datetime.utcnow() + offset

def get_watchlist_resp(location, timezone, dt):

    content = location
    content["timezone"] = timezone["timeZoneName"]
    content["timezoneid"] = timezone["timeZoneId"]
    content["utcoffset"] = timezone["rawOffset"]
    content["datetime"] = utils.dt_to_dict(dt)

    return content
