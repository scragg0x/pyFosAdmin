from gevent import wsgi
from fosadmin import app, manager
import logging


@manager.command
def server(port=5000):
    """ Run production (WSGI) server """
    app.logger.setLevel(logging.INFO)
    wsgi.WSGIServer(('', int(port)), app).serve_forever()


if __name__ == '__main__':
    manager.run(default_command='server')