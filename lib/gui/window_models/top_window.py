from lib.gui import GUI


class TopWindow(GUI):
    """
        Define a kind of template object to construct windows on later
    """

    def __init__(self, conf, file=None):
        super().__init__(conf)
        self.logger_started = False
        self.name = self.__class__.__name__
        print(self.name)
        log = self.get_logger()

        self.config = conf
        grab = self.config.get('gui_settings', 'grab_anywhere')
        if grab == 'None':
            print('Grab is none')
            self._first_time_()

        window = self.qt.Window('Test win', layout=self._layout_(conf), grab_anywhere=grab)
        print(dir(self))
        self.top_window = window

    def _first_time_(self):
        """
        This is run when the system detects no config file or a malformed config

        :return:
        """
        from icons.app_icons import config_icon
        icon = config_icon()

        # Build popup to ask user to config
        message = "It seems that you haven't gone through setting your options yet. Would you like me to open " \
                  "the options window immediately after starting this one time to initialize your config file?"

        # Pop the question
        query = self.qt.PopupYesNo(message, title='Config warning...', keep_on_top=True, icon=icon, location=(475, 325))

        # If
        if str(query).lower() == 'yes':
            self.opts_win_active = True

    @staticmethod
    def _top_menu_():
        menu = [
            ['File', ['Settings::_SETTINGS_BUTTON_']],
            ['Help', ['Docs', ['@softworks.inspyre.tech'], ], ],
        ]
        return menu

    def _button_frame_(self):
        """
        Create a frame for our buttons at the bottom of the window

        :returns: Button frame object
        :rtype:
        """
        b_frame = [
            [self.qt.Button('Make Another', key='dupe'), self.qt.Button('Exit', key='top_win_exit')]
        ]
        return b_frame

    def _sense_frame_(self, config):
        qt = self.qt
        device_name = 'Living Room'
        from lib.sense.info import SenseInfo
        info = SenseInfo()

        if config.get('sense_customize', 'dsp_temp') == 'F':
            temp = info.get_temp_f()
        else:
            temp = info.get_temp(raw=False)

        humidity = round(info.get_humidity())
        humidity = humidity.__str__()

        struct = [[qt.Text(f'Current Interior Temperature in {device_name}'),
                   qt.Text(temp, key='test_field', justification='right'), ],
                  [qt.Text(f'Current humidity in {device_name}'),
                   qt.Text(f"{humidity}%", key='humidity_results', justification='right')],
                  [qt.Text(f"Current barometric pressure in {device_name}"),
                   qt.Text(info.get_pressure(), key='pressure_results'),
                   qt.Text('MB')]
                  ]
        return struct

    def _layout_(self, config):
        qt = self.qt
        struct = [
            [qt.Menu(self._top_menu_())],
            [qt.Text('Welcome to Test API!')],
            [qt.Combo(['Living Room', 'Playroom'])],
            [qt.Frame('', self._sense_frame_(config))],
            [qt.Frame('', list(self._button_frame_()))]
        ]

        return struct
