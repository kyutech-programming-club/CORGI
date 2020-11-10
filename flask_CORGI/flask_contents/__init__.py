from flask import Flask


app = Flask(__name__)
app.config.from_object("flask_contents.config")

import flask_contents.views
