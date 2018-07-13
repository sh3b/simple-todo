# config.py Configuration variables for our Flask app
import os

class Configuration(object):
    """
       Refer http://flask.pocoo.org/docs/0.11/templating/#standard-context
    """""

    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    DEBUG = True

    # Create a unique key for your app.
    # http://flask.pocoo.org/docs/0.11/quickstart/#sessions
    SECRET_KEY = '\x89\xc0\xae\x1f\x7f\x99\x8f\xfc\xc0\x8a\xc6\xad\xdcZC2\x11JLq\xa4\x08b'

    #Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/todo.db' % APPLICATION_DIR
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #Directories
    STATIC_DIR = os.path.join(APPLICATION_DIR, 'static')

    #Set site's name
    SITENAME = 'Todoe'