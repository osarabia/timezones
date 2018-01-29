from flask import request, Response, json
from flask.views import MethodView

from timezones import errors
from timezones import helpers
from timezones.models import CitiesModel
from timezones.validations import validate_watchlist

watchlist = []
unique_watchlist = {}

class WatchList(MethodView):

    def get(self):
        for i in xrange(0, len(watchlist)):
            offset = watchlist[i]["utcoffset"]
            dt = calculate_dt(offset)
            watchlist[i]["datetime"] = dt_to_dict(dt)

        return Response(json.dumps(watchlist), mimetype="application/json")

    def post(self):
        validated_data = validate_watchlist(request.json)
        city_id = validated_data["city_id"]
        location = CitiesModel.get_city_location(city_id)

        timezone = helpers.fetch_timezone(timestamp=validated_data["timestamp"],
                                          **location)

        dt = helpers.new_utc(timezone["rawOffset"])
        resp = helpers.get_watchlist_resp(location, timezone, dt)
        watchlist.append(resp)
        unique_watchlist[city_id] = len(watchlist) - 1

        return Response(json.dumps(resp),
                        mimetype="application/json")

    def delete(self, city_id):
        if city_id in unique_watchlist:
            index = unique_watchlist[city_id]
            watchlist.pop(index)
            del unique_watchlist[city_id]

            for i in xrange(index, len(watchlist)):
                idd = watchlist[i]["city_id"]
                unique_watchlist[idd] = i

            return Response("", mimetype="application/json",
                            status="204")

        return Response(json.dumps({"message": "Not Found"}),
                        mimetype="application/json",
                        status="404")
