from flask import request, Response, json, current_app
from flask.views import MethodView

class Cities(MethodView):

    def get(self):
        if "startswith" in request.args:
            city = request.args["startswith"].lower()
            cities = current_app.CitiesModel.fetch_cities(city)

            return Response(json.dumps(cities), mimetype="application/json")

        return Response(json.dumps([]), mimetype="application/json")
