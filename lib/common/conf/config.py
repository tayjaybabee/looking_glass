class Config(object):

    def __init__(self, custom_file=None):
        import logging
        log = logging.getLogger
        from configparser import ConfigParser
        self.parser = ConfigParser()
        self.parser.read('config.ini')
        self.config = self.parser

    def write(self):
        import os
        working_conf = open(os.getcwd() + '/conf/config.ini')
        self.config.write(working_conf)
        working_conf.close()