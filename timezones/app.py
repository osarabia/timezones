
from timezones.utils import get_file, get_db_conn, dt_to_dict
from timezones.helpers import fetch_cities, fetch_city_location,\
                              fetch_timezone, validate_timestamp_input,\
                              calculate_dt
from timezones.responses import invalid_user_input, add_watchlist_resp

from flask import Flask, Response, request, json

app = Flask(__name__, static_url_path='/static')
app.config.from_object(__name__)

db_conn = get_db_conn()

watchlist = []
unique_watchlist = {}


@app.route('/', methods=['GET'])
def index():
    content = get_file("index.html")

    return Response(content, mimetype="text/html")


@app.route('/cities', methods=['GET'])
def cities():
    if "city" in request.args:
        cities = fetch_cities(db_conn, request.args["city"])

        return Response(json.dumps(cities), mimetype="application/json")

    return Response(json.dumps([]), mimetype="application/json")


@app.route('/watchlist/cities/', methods=['GET'])
def get_watchlist():
    for i in range(0, len(watchlist)):
        offset = watchlist[i]["utcoffset"]
        dt = calculate_dt(offset)
        watchlist[i]["datetime"] = dt_to_dict(dt)

    return Response(json.dumps(watchlist), mimetype="application/json")


@app.route('/watchlist/cities/<int:city_id>', methods=['POST'])
def add_watchlist(city_id):
    location = fetch_city_location(db_conn, city_id)
    if location is not None and \
       city_id not in unique_watchlist and \
            request.json is not None:
        is_valid, timestamp = validate_timestamp_input(request.json)

        if is_valid:
            timezone = fetch_timezone(timestamp=timestamp, **location)
            if timezone is not None:
                dt = calculate_dt(timezone["rawOffset"])

                resp = add_watchlist_resp(location, dt, timezone)
                watchlist.append(resp)
                unique_watchlist[city_id] = len(watchlist) - 1

                return Response(json.dumps(resp),
                                mimetype="application/json")

    return invalid_user_input()


@app.route('/watchlist/cities/<int:city_id>', methods=["DELETE"])
def delete_watchlist(city_id):
    if city_id in unique_watchlist:
        index = unique_watchlist[city_id]
        watchlist.pop(index)
        del unique_watchlist[city_id]

        for i in range(index, len(watchlist)):
            city_id = watchlist[i]["city_id"]
            unique_watchlist[city_id] = i

    return Response("", mimetype="application/json",
                    status="204")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
