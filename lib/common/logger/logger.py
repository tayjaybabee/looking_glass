#!/usr/bin/env python3
class Logger(object):
    """Logger library for the ITSM application"""


    def __init__(self, name, config=None):
        self.config = config
        self.name = str( )

        import logging
        from colorlog import ColoredFormatter


        def setup_logger(self, caller_name):
            """Return a logger with a default ColoredFormatter."""
            if not caller_name:
                self.caller_name = 'senseMonGUI'
            else:
                caller_name = '{0}.{1}'.format(na)
                formatted_name = 'senseMonGUI' + '.' + '%s' % callerName
            formatter = ColoredFormatter(
                "%(bold_cyan)s%(asctime)-s%(reset)s%(log_color)s::%(name)-14s::%(levelname)-10s%(reset)s%(blue)s%(message)-s",
                datefmt=None,
                reset=True,
                log_colors={
                    'DEBUG':    'bold_cyan',
                    'INFO':     'bold_green',
                    'WARNING':  'bold_yellow',
                    'ERROR':    'bold_red',
                    'CRITICAL': 'bold_red',
                }
            )

            logger = logging.getLogger(formatted_name)
            handler = logging.StreamHandler()
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.DEBUG)
            logger.info(f'Logger started for %s' % callerName)

            return logger

