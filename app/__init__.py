from flask import Flask

from app.ext import init_ext


def create_app():
    app= Flask(__name__)
    init_ext(app)
    return app