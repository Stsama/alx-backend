#!/usr/bin/env python3
"""
Basic Babel setup
"""

from flask import Flask, render_template
from babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/", methods=['GET'], strict_flashes=False)
def hello_world():
    """
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)
