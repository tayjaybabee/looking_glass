from lib.gui import GUI


class OptsWindow(GUI):
    """
    Class containing the information for the Options Window
    """

    def __init__(self, config):
        import PySimpleGUIQt as qt
        self.qt = qt
        self.config = config
        """
        Initialize a new instance of the options window

        :param config: The config object from the App class
        """

        self.opts_win = qt.Window('Options', layout=self.main_layout(), )

    @staticmethod
    def _localization_frame_():
        """
        This frame helps us group settings related to region-specific measurement systems

        :return:
        """

        import PySimpleGUIQt as qt
        frame = [
            [qt.Text('Primary Temperature Unit:',
                     justification='left'),
             qt.Radio('Fahrenheit',
                      group_id='sense_customize.dsp_temp',
                      default=True),
             qt.Radio('Celsius',
                      group_id='sense_customize.dsp_temp'),
             qt.Radio('Kelvin',
                      group_id='sense_customize.dsp_temp')]
        ]

        return frame

    def _weather_api_frame_(self):
        """
        This frame helps us group settings related to the weather API together to present in the GUI for the end-user


        :return:
        """
        import PySimpleGUIQt as qt

        struct = [
            [qt.Text('DarkSky API Key:', justification='left'),
             qt.InputText(self.config.get("weather_api_settings", "key"), key='weather_api_settings.key',
                          justification='right')],
            [qt.Button('Reset', key='reset_fields'), qt.Button('Check Key', key='check_api_key')]
        ]

        return struct

    def geolocale_frame(self, opt_name=None):
        """
        This frame helps us group settings related to the geo-location together to present in the GUI for the end-user

        :return:
        """
        qt = self.qt

        struct = []

        for option in self.config.options(section='location'):
            opt_name = str(option).replace('_', ' ')
            opt_name = opt_name.capitalize()
            new_line = [qt.Text(opt_name, justification='left'),
                        qt.InputText(f'{self.config.get("location", option)}')]

            struct.append(new_line)

        return struct

    def main_layout(self):
        """
        The main layout structure logic for the preferences window

        :return:
        """
        import PySimpleGUIQt as qt
        # noinspection SpellCheckingInspection
        layout = [
            [qt.Frame('', self._localization_frame_(), background_color='#00c2c7'),
             qt.Frame('', self._weather_api_frame_(), background_color='#97ebdb')],
            [qt.Frame('', self.geolocale_frame(), background_color='#005582')],
            [qt.Button('Cancel', key='opts_win_cancel'), qt.Button('OK', key='opts_win_ok')]

        ]

        return layout

    def start(self):
        log = self.log
        log.debug()
        self.opts_win_active = True
