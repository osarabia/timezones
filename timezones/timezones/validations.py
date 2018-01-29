
from timezones.exceptions import MissingField, UnExpectedType

def validate_watchlist(payload):
    if payload is not None:
        if "city_id" not in payload:
            raise MissingField("missing field city_id")

        if "timestamp" not in payload:
            raise MissingField("missing field timestamp")

        try:
            city_id = int(payload["city_id"])
        except Exception:
            raise UnExpectedType("expecting number field city_id")

        try:
            timestamp = int(payload["timestamp"])
        except Exception:
            raise UnExpectedType("expecting number field timestamp")

        return {
                   "city_id": city_id,
                   "timestamp": timestamp
               }

    raise MissingField("missing fields city_id and timestamp")
