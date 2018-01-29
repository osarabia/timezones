
from flask import jsonify

from timezones import app
from timezones.exceptions import DoesNotExists, MissingField, UnExpectedType, ServiceFailed

@app.errorhandler(DoesNotExists)
def handle_does_not_exists(error):
    resp = jsonify(error.to_dict())
    resp.status_code = 404

    return resp

@app.errorhandler(MissingField)
def handle_missing_field(error):
    resp = jsonify(error.to_dict())
    resp.status_code = 401

    return resp

@app.errorhandler(UnExpectedType)
def handle_unexpected_type(error):
    resp = jsonify(error.to_dict())
    resp.status_code = 401

    return resp

@app.errorhandler(ServiceFailed)
def handle_service_failed(error):
    resp = jsonify(error.to_dict())
    resp.status_code = 500

    return resp

