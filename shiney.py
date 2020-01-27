class App:
    """
    A class for the main app

    Options:
        --config-file=
    """



    def __init__(self):
        from lib.common.conf.config import Config
        from lib.common.logger.logger import Logger

        self.name = 'senseMonGUI'
        self.log = Logger(name=self.name)

        conf_init = Config()
        conf = conf_init.parser
        self.conf = conf
        print(self.conf)
        self.run(config=self.conf)

    def run(self, config=None):
        from window_models.top_window import TopWindow

        builder = TopWindow(config=config)
        window = builder.window

        opts_win_active = False

        while True:
            event, values = window.read(timeout=100)
            if event is None or event == 'top_win_exit':
                exit()

            if not opts_win_active and event == 'Settings::_SETTINGS_BUTTON_':
                from window_models.opts_window import OptsWindow
                opts_win_active = True
                opts_builder = OptsWindow(config=config)
                opts_win = opts_builder.window

            while opts_win_active:
                event2, values2 = opts_win.read(timeout=100)
                if event2 is None or event2 == 'opts_win_cancel':
                    opts_win.close()
                    opts_win_active = False

                if event2 == 'opts_win_ok':
                    from lib.common.conf.config import Config
                    Config.write(config)




app = App()

