import click
from config.config import *
from flask import Flask, redirect, url_for

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

@app.route("/")
def _redirect():
    return "hello world"