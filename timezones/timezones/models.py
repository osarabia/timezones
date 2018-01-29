
from timezones import db
from timezones.countries import countries
from timezones.exceptions import DoesNotExists

SQL_CITIES = "select city_id, name, country from cities where name like %s limit 10"
SQL_CITY = "select city_id, country, name, lat, lon from cities where city_id=%s"

class _Cities(object):
    def __init__(self, conn):
        self.conn = conn

    def fetch_cities(self, name):
        """Filter Cities by Name"""

        name = name + "%"
        cities = []
        with self.conn.cursor() as cursor:
            cursor.execute(SQL_CITIES, (name,))
            if cursor.rowcount > 0:
                for c in cursor.fetchall():
                    country = countries.get(c[2], c[2])
                    cities.append({"id": c[0], "name": c[1], "country": country})

        return cities

    def get_city_location(self, city_id):
        """Get City Location By Id"""

        with self.conn.cursor() as cursor:
            cursor.execute(SQL_CITY, (city_id,))
            if cursor.rowcount > 0:
                record = cursor.fetchone()

                return {
                           'city_id': record[0],
                           'country': countries.get(record[1], record[1]),
                           'city': record[2],
                           'lat': record[3],
                           'lon': record[4]
                       }

        raise DoesNotExists()

CitiesModel = _Cities(db)
