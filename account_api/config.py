'''
Config info for autodb.
'''
import os
root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# let's add a random comment

class Config:
    DEBUG = True
    TESTING = False

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
