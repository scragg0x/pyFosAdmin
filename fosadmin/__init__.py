from flask import Flask, render_template
from flask.ext.script import Manager
from foscontrol import Cam

import base64
import os
import json

app = Flask(__name__)
app.debug = True

manager = Manager(app)


def load_cam(config=None):
    if config:
        # Persist and use
        pass
    else:
        f = open(os.path.dirname(os.path.realpath(__file__)) + "/../config.json")
        config = json.loads(f.read())
        f.close()

    return Cam(config.get('PROTOCOL', 'http'),
               config.get('HOST'),
               config.get('PORT', 88),
               config.get('USERNAME', 'admin'),
               config.get('PASSWORD', ''))

cam = load_cam()


@app.route("/")
def home():
    return render_template('index.html', cam=cam)


@app.route("/snapshot", methods=['POST'])
def snapshot():
    return base64.b64encode(cam.snapPicture()[0])


@app.route("/setup")
def setup():
    return render_template('setup.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/move/<action>", methods=['POST'])
def move(action):
    if action == 'stop':
        cam.ptzStopRun()
    else:
        cam.ptzMove(action)
