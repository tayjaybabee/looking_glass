class Config(object):

    def __init__(self, custom_file=None):
        from configparser import ConfigParser
        self.parser = ConfigParser()
        self.parser.read('config.ini')
        self.config = self.parser

    def write(self):
        import os
        print(os.getcwd())
        working_conf = open('conf/config.ini')
        self.config.write(working_conf)
        working_conf.close()