from timezones import app, utils
from timezones.cities.views import Cities
from timezones.watchlist.views import WatchList

from flask import Response

cities_view = Cities().as_view("cities")
watchlist_view = WatchList().as_view("watchlist")

def index():
    content = utils.get_file("index.html")

    return Response(content, mimetype="text/html")


app.add_url_rule('/', view_func=index, methods=['GET',])

app.add_url_rule('/cities/', view_func=cities_view
                           , methods=['GET',])

app.add_url_rule('/watchlist/', view_func=watchlist_view
                           , methods=['GET', "POST",])

app.add_url_rule('/watchlist/<int:city_id>/', view_func=watchlist_view
                           , methods=['DELETE',])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

