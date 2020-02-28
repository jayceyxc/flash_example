from flask import Blueprint


def register(app):
    api_bp = Blueprint('api', __name__, url_prefix='/api')
    app.register_blueprint(api_bp)
