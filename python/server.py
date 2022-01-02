from flask import Flask, send_from_directory, request, make_response
from functools import wraps, update_wrapper
from datetime import datetime
import sys
import time
import os.path
import requests
import paramiko
from xml.etree import ElementTree
from flask_socketio import SocketIO, emit


def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.now()
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response
        
    return update_wrapper(no_cache, view)

app = Flask(__name__)
socketio = SocketIO(app)

# Path for our main Svelte page
@app.route("/")
@nocache
def base():
    return send_from_directory('../dist', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
@nocache
def home(path):
    if os.path.exists('node_modules/@fontsource/'+path):
      return send_from_directory('node_modules/@fontsource', path)
    else:
      return send_from_directory('../dist', path)

@app.route("/rand")
def hello():
    return str(12345)

@socketio.on('connect')
def connect():
    print('Client connected')
    return

@socketio.on('disconnect')
def disconnect():
    print('Client disconnected')
    return

@socketio.on('message')
def test_message(msg):
    print ("Message received:", msg)
    emit('message', 'hello from server')
    return

if __name__ == "__main__":
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(host='0.0.0.0', port=5010, debug=True)
