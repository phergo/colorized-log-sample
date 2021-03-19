# -*- coding: utf-8 -*-
# @Author: phergo
# @Date: 2021-03-18 21:25:00

import logging

import mypackage  # Colorized logger is initialized here.

#
# Display colorized log.
#
logging.debug('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
logging.info('Donec sodales dolor tortor, ornare lobortis enim vulputate quis.')
logging.warning('Integer quis leo vitae lorem aliquet facilisis.')
logging.error('Ut eget sodales magna.')
logging.critical('Nulla facilisi.')
