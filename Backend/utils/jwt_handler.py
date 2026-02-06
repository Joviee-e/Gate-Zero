from flask_jwt_extended import create_access_token as _create_token


def create_access_token(identity: str):
    """
    Wrapper around flask-jwt-extended token creation
    """

    return _create_token(identity=identity)
