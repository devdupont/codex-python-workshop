"""
App routing and view functions
"""

from functools import wraps
from typing import Callable

from flask import jsonify, render_template, request, Response

from crimes import app
from crimes.models import Crime


def check_auth(func: Callable) -> Callable:
    """
    Checks for a valid Authorization token in the request
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        auth = request.headers.get("Authorization")
        if not auth:
            return "", 401
        # Removes any value prefixes
        if auth.split()[-1] != "123abc":
            return "", 403
        return func(*args, **kwargs)

    return wrapper


@app.route("/")
def index() -> str:
    """
    Static string home page
    """
    return "Hello, Python!!!"


@app.route("/json")
@check_auth
def data_payload() -> Response:
    """
    Sample JSON response that checks for an auth token
    """
    return jsonify({"data": True})


@app.route("/hello")
@app.route("/hello/<name>")
def hello(name: str = None) -> Response:
    """
    Says hello with an optional name parameter from the URL path
    """
    # render_template looks for the file in the templates folder
    # Variables are passed to the template as keyword arguements
    return render_template("hello.html", name=name)


def get_crimes(ctype: str = None) -> [Crime]:
    """
    Return all crimes matching a category type or the first ten
    """
    if ctype:
        return Crime.query.filter_by(offense_category=ctype).all()
    return Crime.query.limit(10).all()


@app.route("/crimes", methods=["GET", "POST"])
@app.route("/crimes/type/<ctype>")
def crimes(ctype: str = None) -> Response:
    """
    Render the Crime list and search HTML page
    """
    # Pull the type value from the HTML form if a POST request
    if request.method == "POST":
        ctype = request.form["ctype"]
    return render_template(
        "crimes.html",
        ctype=ctype,
        count=Crime.query.count(),
        crimes=get_crimes(ctype),
    )


@app.route("/json/crimes")
@app.route("/json/crimes/type/<ctype>")
def crimes_data(ctype: str = None) -> Response:
    """
    Like "crimes" but returns JSON representations
    """
    return jsonify([crime.serialized for crime in get_crimes(ctype)])


@app.route("/name", methods=["POST"])
def name_post() -> Response:
    """
    Returns the length of a name in a POST payload
    """
    name = request.json["name"]
    return jsonify({
        "name": name,
        "count": len(name)
    })
