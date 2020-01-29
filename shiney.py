class App:
    """
    A class for the main app

    ToDo:
        - add command-line arguments
    """

    def __init__(self):

        from lib.common.conf.config import Config
        from lib.common.logger.logger import Logger
        self.logger = Logger()

        self.log = self.logger.setup_logger()

        conf_init = Config()
        conf = conf_init.parser
        self.conf = conf
        print(self.conf)
        self.run(config=self.conf)

    def run(self, config=None):
        from window_models.top_window import TopWindow
        import logging
        from lib.common.logger.logger import Logger

        logger = Logger()

        logger_name = logger.name_registrar('App')

        log = logging.getLogger(logger_name)

        log.debug('Getting TopWindow')
        builder = TopWindow(config=config)

        log.debug('Instantiating TopWindow')
        window = builder.window

        log.debug("Setting all other windows to inactive")
        opts_win_active = False

        log.debug('Show window!')

        units = config.get('sense_customize', 'dsp_temp') # dsp = display
        print(units)

        while True:
            event, values = window.read(timeout=100)
            if event is None or event == 'top_win_exit':
                log.info('User indicated a desire to exit.')
                exit()

            # If the options window isn't already active and the user hit Settings on the main window then read the
            # options window and wait for the user to do something else.
            if not opts_win_active and event == 'Settings::_SETTINGS_BUTTON_':
                log.info('User indicated a desire to enter the Settings menu')

                log.debug('Preparing window')
                from window_models.opts_window import OptsWindow
                opts_win_active = True
                log.debug('Options Window set to active.')
                log.debug('Calling Options Window builder')
                log.debug(f'Passing builder a config with these sections {config.sections()}')
                opts_builder = OptsWindow(config=config)
                opts_win = opts_builder.window

            # Read the window and wait for event
            counter = 0
            while opts_win_active:
                event2, values2 = opts_win.read(timeout=100)



                # If the user presses the X button or presses 'cancel' the options window will close.
                if event2 is None or event2 == 'opts_win_cancel':
                    log.debug('User cancelled or closed window')
                    log.debug('Closing Options Window, ignoring changes')
                    opts_win.close()
                    opts_win_active = False
                    log.debug('Options window closed and set to inactive status. No changes saved.')

                # If the user presses 'OK' we call on the Config class to write the current config to a file
                if event2 == 'opts_win_ok':
                    log.debug('User indicated a desire to exit the config window')

                    from lib.common.conf.config import Config
                    Config.write(config)


app = App()

