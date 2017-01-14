import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-will-change'


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class ProdConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
