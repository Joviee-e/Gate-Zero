from flask import jsonify


def success(message=None, data=None, status=200):
    payload = {}

    if message:
        payload["message"] = message

    if data is not None:
        payload["data"] = data

    return jsonify(payload), status


def error(message, status=400):
    return jsonify({"error": message}), status
