'''
Config info for autodb.
'''
import os
root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# let's add a random comment

class Config:
    DEBUG = True
    TESTING = False

    # import ipdb; ipdb.set_trace()
    SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production(Config):
    """
    Production config
    """
    DEBUG = False


class Development(Config):
    """
    Development config
    """
    pass

class Testing(Config):
    """
    Testing config
    """
    pass
    # SERVER_NAME = 'localhost'
    # TESTING = True
    # SQLALCHEMY_DATABASE_URI = F'sqlite:///{root}/autodb/test.db'
    # # SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.environ["HOME"]}/Dropbox/sandbox/python/flasks/autodb/test.db'
