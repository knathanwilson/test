
from flask import Flask, request, redirect, Response, make_response, url_for

app = flask(__name__)


@app.route('/')
def index(): return 'this is working???'
