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

            # If the user presses "Fetch Device Data" the system will check if they have a device to fetch data from,
            # and if they do; run operations that would populate the fields in the gui and refresh

            if event == 'fetch_device_info':
                print(event, values)
                if 'Add Device' in values:
                    print(values)
                    from lib.gui.popups.warnings import no_device_for_fetch as no_device_popup
                    if no_device_popup():
                        continue
                    else:
                        break

            # If the options window isn't already active and the user hit Settings on the main window then read the
            # options window and wait for the user to do something else.
            if not gr_ui.opts_win_active and event == 'Settings::_SETTINGS_BUTTON_':
                opts_win = gr_ui.options_window(self.config)
                gr_ui.opts_win_active = True

            # Read the window and wait for event
            counter = 0
            while gr_ui.opts_win_active:
                event2, values2 = opts_win.read(timeout=100)

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
                    opts_win.close()
                    gr_ui.opts_win_active = False

    def __init__(self):
        self.logger_started = False
        import lib.common.logger as logger
        from lib.common.logger.caller import identify
        name = identify('', True)
        self.log = logger.start(name)
        from lib.common.conf.config import Config

        looking_glass = LookingGlass()

        self.config = Config().config

        self.run()


app = App()
