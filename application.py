import flask
import requests
import json
from flask import Flask, render_template, url_for
app = flask.Flask(__name__)
app.config["DEBUG"] = True
#new

@app.route('/terms', methods=['GET'])
def parms():
    return ("Terms and condition")