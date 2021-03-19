# -*- coding: utf-8 -*-
# @Author: phergo
# @Date: 2021-03-18 21:19:00
# "major.minor.micro" versioning.
__version__ = '0.1.0'

import logging
import logging.config
import os
import yaml

#
# Initialize logger.
#
_LOG_CONFIG_FILE = './logging.yaml'

try:
    with open(_LOG_CONFIG_FILE, 'rt') as f:
        config = yaml.safe_load(f.read())
    # Make sure the logging folder exists, if any.
    handlers = config.get('handlers')
    if handlers.get('file_handler'):
        filename = handlers.get('file_handler').get('filename')
        if filename:
            dirname = os.path.dirname(filename)
            if not os.path.isdir(dirname):
                os.makedirs(dirname)
    # Initialize logger
    logging.config.dictConfig(config)

except Exception as err:
    logging.basicConfig(level=logging.INFO)
    logging.warning(f'Error reading `{_LOG_CONFIG_FILE}`; using basic config.')
