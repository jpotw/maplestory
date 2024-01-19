from flask import Flask
from flask_wtf.csrf import CSRFProtect

def create_app():
    app = Flask(__name__)
    csrf = CSRFProtect(app)
    app.config['SECRET_KEY'] = 'ASDWSAasdfsed'
    app.debug = True

    from maplestory.views import upload_views
    app.register_blueprint(upload_views.bp)
    return app
