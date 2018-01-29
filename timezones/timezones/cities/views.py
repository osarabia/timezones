from flask import request, Response, json
from flask.views import MethodView

from timezones import errors
from timezones.models import CitiesModel

class Cities(MethodView):

    def get(self):
        if "startswith" in request.args:
            city = request.args["startswith"].lower()
            cities = CitiesModel.fetch_cities(city)

            return Response(json.dumps(cities), mimetype="application/json")

        return Response(json.dumps([]), mimetype="application/json")
