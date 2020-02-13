from looking_glass import App


class Config(App):

    def check_existing(self):
        log = self.log
        from pathlib import Path
        file = 'config.ini'
        path = self.config_dir
        filepath = Path(str(file + path))
        log.debug(f'Default file path is: "{filepath}"')
        if filepath.is_file():
            self.conf_file = filepath
            return True
        return False

    def load(self, fallback=False):
        from configparser import ConfigParser
        from os import getcwd

        parser = ConfigParser()

        log = self.log

        if fallback:
            log.info('Unable to find a previous config file. Loading example_conf.ini')
            conf_file = str(f"{getcwd()}/docs/example_conf.ini")
        else:
            conf_file = self.conf_file

        log.debug(f'Loading config file: "{conf_file}"')

        parser.read(conf_file)

        log.debug(f'Loaded file. It has the following sections: "{parser.sections()}"')
        log.debug('Making config object accessible')
        self.config = parser

    def __init__(self, custom_conf=None):
        import os
        from configparser import ConfigParser
        import glob

        parser = ConfigParser()
        import logging
        log = logging.getLogger(str(f'LookingGlass.App.{self.__class__.__name__}'))
        self.log = log
        log.debug(f'Logger started for {self.__class__.__name__}')

        self.config_dir = str(f"{os.getcwd()}/conf/")
        config_dir = self.config_dir
        log.debug(f"Default 'config' directory is {config_dir}")
        self.conf_file = None

        if self.check_existing():
            self.load()
        else:
            self.load(fallback=True)

        # file_names = self.filepath_list_build(file_names)
        #
        # log.debug(f'Final paths for default .ini locations: {file_names}')
        #
        # log.debug(f'Checking to see if user provided a custom config file path as an argument...')
        # if custom_conf is not None:
        #     log.info(f'Caught argument to specify config file path.')
        #     file_names.insert(0, custom_conf)
        #
        # found = parser.read(file_names)
        # self.config = parser
        # print(parser.sections())
        # missing = set(file_names) - set(found)
        #
        # print('Found config files:', sorted(found))
        # print('Missing files     :', sorted(missing))

    @staticmethod
    def write(conf):
        import os
        with open(os.getcwd() + '/conf/config.ini', 'w') as conf_file:
            conf.write(conf_file)


if __name__ == "__main__":
    config = Config()
else:
    print(__name__ + ' is being imported, but not running __init__')
