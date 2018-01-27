
import requests

from datetime import datetime
from datetime import timedelta

from countries import countries

SQL_CITIES = "select city_id, name, country from cities where name like '{city}%' limit 10"
SQL_CITY = "select city_id,country,name,lat,lon from cities where city_id={city_id}"
TIMEZONE_URL = "https://maps.googleapis.com/maps/api/timezone/json?location={lat},{lon}&timestamp={timestamp}&key=AIzaSyBT92tKXjQUXigZPUy1cGYGceRkaUekT4A"


def fetch_cities(conn, city):
    cities = []
    with conn.cursor() as cursor:
        cursor.execute(SQL_CITIES.format(city=city))
        if cursor.rowcount > 0:
            for c in cursor.fetchall():
                country = countries.get(c[2], c[2])
                cities.append({"id": c[0], "name": c[1], "country": country})

    return cities


def fetch_city_location(conn, city_id):
    with conn.cursor() as cursor:
        cursor.execute(SQL_CITY.format(city_id=city_id))
        if cursor.rowcount > 0:
            record = cursor.fetchone()

            return {
                       'city_id': record[0],
                       'country': countries.get(record[1], record[1]),
                       'city': record[2],
                       'lat': record[3],
                       'lon': record[4]
                   }

    return None


def fetch_timezone(lat, lon, timestamp, **kwargs):
    url = TIMEZONE_URL.format(lat=lat, lon=lon, timestamp=timestamp)
    resp = requests.get(url)
    try:
        content = resp.json()
    except Exception:

        return None

    if "status" not in content and timezone["status"] != "OK":

        return None

    return content


def validate_timestamp_input(payload):
    if "timestamp" in payload:
        timestamp = payload["timestamp"]

        if isinstance(timestamp, int):
            return True, timestamp

    return false, None


def calculate_dt(utc_offset):
    offset = timedelta(seconds=utc_offset)

    return datetime.utcnow() + offset
