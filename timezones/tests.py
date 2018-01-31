
from timezones import create_app
from timezones.exceptions import DoesNotExists

import unittest
import json

data = [{"id": 1, "name": "hermosillo", "country": "Mexico", "lat": "29.089186", "lon": "-110.96133"},
        {"id": 2, "name": "new york", "country": "United States Of America", "lat": "40.730610", "lon": "-73.935242"},
        {"id": 3, "name": "san francisco", "country": "United States of America", "lat": "37.77493", "lon": "-122.419416"},
        {"id": 4, "name": "mexico city", "country": "Mexico", "lat": "19.432608", "lon": "-99.133208"}]

class _CitiesModel(object):
     def fetch_cities(self, city):
         return data

     def get_city_location(self, city_id):
         for ct in data:
             if ct["id"] == city_id:
                 return ct

         raise DoesNotExists()


class TestCitiesView(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        #Fake CitiesModel
        self.app.CitiesModel = _CitiesModel()

    def test_retrieve_cities(self):
        with self.app.test_client() as c:
            resp = c.get("/cities/")
        self.assertEqual(200, resp.status_code)

    def test_retrieve_cities_by_name(self):
        with self.app.test_client() as c:
            resp = c.get("/cities/?startswith=her")
        self.assertEqual(200, resp.status_code)

class TestWatchListView(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        #Fake CitiesModel
        self.app.CitiesModel = _CitiesModel()

    def test_add_watchlist(self):
        with self.app.test_client() as c:
            payload = {"city_id":1, "timestamp": 1516896804}
            resp = c.post("/watchlist/", data=json.dumps(payload), content_type="application/json")
        self.assertEquals(200, resp.status_code)

    def test_retrieve_watchlist(self):
        with self.app.test_client() as c:
            payload = {"city_id":1, "timestamp": 1516896804}
            c.post("/watchlist/", data=json.dumps(payload), content_type="application/json")
            resp = c.get("/watchlist/")
        content = json.loads(resp.get_data())
        self.assertEqual(content[0]["name"], "hermosillo")

    def test_delete_watchlist(self):
        with self.app.test_client() as c:
            payload = {"city_id":1, "timestamp": 1516896804}
            c.post("/watchlist/", data=json.dumps(payload), content_type="application/json")
            resp = c.delete("/watchlist/1/")
        self.assertEquals(resp.status_code, 204)

if __name__ == "__main__":
    unittest.main()
