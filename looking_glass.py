class LookingGlass:
    pass


class App(LookingGlass):
    """
    A class for the main app

    ToDo:
        - add command-line arguments
    """

    @staticmethod
    def _config_():
        from lib.common.conf.config import Config
        config = Config().config
        return config

    # noinspection SpellCheckingInspection
    def run(self):
        from lib.gui import GUI

        gr_ui = GUI(self.config)

        opts_win = gr_ui.opts_window(self.config)

        log = self.log

        log.debug('Getting TopWindow')
        top_window = gr_ui.top_window(self.config)

        log.debug('Instantiating TopWindow')

        log.debug("Setting all other windows to inactive")

        log.debug('Show window!')

        while True:
            event, values = top_window.read(timeout=100)
            if event is None or event == 'top_win_exit':
                log.info('User indicated a desire to exit.')
                exit()

            # If the options window isn't already active and the user hit Settings on the main window then read the
            # options window and wait for the user to do something else.
            if not gr_ui.opts_win_active and event == 'Settings::_SETTINGS_BUTTON_':
                gr_ui.opts_win_active = True

            # Read the window and wait for event
            counter = 0
            while gr_ui.opts_win_active:
                event2, values2 = gr_ui.opts_win.read(timeout=100)

                # If the user presses the X button or presses 'cancel' the options window will close.
                if event2 is None or event2 == 'opts_win_cancel':
                    log.debug('User cancelled or closed window')
                    log.debug('Closing Options Window, ignoring changes')
                    opts_win.close()
                    gr_ui.opts_win_active = False
                    log.debug('Options window closed and set to inactive status. No changes saved.')

                # If the user presses 'OK' we call on the Config class to write the current config to a file
                if event2 == 'opts_win_ok':
                    log.debug('User indicated a desire to exit the config window')

                    from lib.common.conf.config import Config
                    Config.write(self.config)

                # If the user presses 'Test Key' we test their API key
                if event2 == 'check_api_key':
                    import PySimpleGUI as gui
                    eprint = gui.EasyPrint()
                    eprint('Checking API key!')

    def __init__(self):
        self.logger_started = False
        import lib.common.logger as logger
        self.log = logger.start()
        from lib.common.conf.config import Config

        self.config = Config().config

        self.run()


if __name__ == "__main__":
    app = App()
else:
    print('Being imported, but not running __init__')
