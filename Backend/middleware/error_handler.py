from flask import jsonify
from werkzeug.exceptions import HTTPException


# ---------------------------------------------------
# GLOBAL ERROR HANDLER REGISTRATION
# ---------------------------------------------------

def register_error_handlers(app):
    """
    Register global error handlers on Flask app.
    """

    @app.errorhandler(HTTPException)
    def handle_http_exception(e):
        return jsonify({
            "error": e.name,
            "message": e.description
        }), e.code

    @app.errorhandler(404)
    def not_found(e):
        return jsonify({
            "error": "Not Found",
            "message": "Requested resource does not exist"
        }), 404

    @app.errorhandler(500)
    def internal_error(e):
        return jsonify({
            "error": "Internal Server Error",
            "message": "Something went wrong"
        }), 500
