from flask import Flask, render_template
from flask.ext.script import Manager
from foscontrol import Cam

import config
import base64

app = Flask(__name__)
app.debug = True

manager = Manager(app)

cam = Cam(config.protocol, config.host, config.port, config.username, config.password)


@app.route("/")
def home():
    return render_template('index.html', cam=cam)


@app.route("/snapshot", methods=['POST'])
def snapshot():
    return base64.b64encode(cam.snapPicture()[0])


@app.route("/move/<action>", methods=['POST'])
def move(action):
    if action == 'stop':
        cam.ptzStopRun()
    else:
        cam.ptzMove(action)
