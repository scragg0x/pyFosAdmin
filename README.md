# pyFosAdmin

Simple FosCam UI that uses [pyFosControl](https://github.com/MStrecke/pyFosControl)

![Sample Screenshot](https://dl.dropboxusercontent.com/u/13941904/screenshots/foscamadmin-01.png)

## Install
```
# Linux global install (recommend using virtualenv)
sudo pip install -r requirements.txt
```

## Config

Create a ```config.py``` file in ```fosadmin```

Sample config.py
```
username = 'admin'
password = ''
host = '192.168.1.246'
port = 88
protocol = 'http'
```

## Running

Browse to ```http://127.0.0.1:5000```

Default port is 5000

VLC plugin required for live stream.  I couldn't get Chrome to work, just used Firefox.

## TODO

Bunch o' stuff