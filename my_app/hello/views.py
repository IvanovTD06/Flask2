from my_app.hello.models import MESSAGES
from flask import Blueprint

hello = Blueprint("Hello", __name__)

@hello.route("/")
def hello_world():
    return MESSAGES["default"]

@hello.route("show/<key>")
def get_message(key):
    return MESSAGES.get(key) or f'{key} not found!'