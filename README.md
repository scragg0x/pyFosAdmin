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