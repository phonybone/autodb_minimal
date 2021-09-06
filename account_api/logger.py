import os
import logging
import logging.config


lpath = os.path.join(os.path.dirname(__file__), 'logging.conf')
assert os.path.exists(lpath), f"{lpath}: no such file"
logging.config.fileConfig(lpath)
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

logging.getLogger('sqlalachemy.engine').setLevel(logging.INFO)
