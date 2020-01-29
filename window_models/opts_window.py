class OptsWindow(object):
    """
    Class containing the information for the Options Window
    """



    def _localization_frame_(self):
        import PySimpleGUIQt as qt
        frame = [
            [qt.Text('Primary Temperature Unit:', justification='left'),
             qt.Radio('Fahrenheit', group_id='temp_unit', default=True), qt.Radio('Celsius', group_id='temp_unit'),
             qt.Radio('Kelvin', group_id='temp_unit')
             ]
        ]
        return frame

    def weather_api_frame(self, config=None):
        import PySimpleGUIQt as qt

        struct = [
            [qt.Text('DarkSky API Key:', justification='left'), qt.InputText('', key='darksky_api_key_input', justification='right')],
            [qt.Button('Reset', key='reset_fields'), qt.Button('Check Key', key='check_api_key')]
        ]

        return struct

    def geolocale_frame(self):
        import PySimpleGUIQt as qt

        struct = [
            [qt.Text('Street Address:', justification="left"), qt.InputText('', key='input_st_address')],
            [qt.Text('City:', justification='left'), qt.InputText('', key='input_city')],
            [qt.Text('State:', justification='left'), qt.InputText('', key='input_state')],
            [qt.Text('Lat:', justification='left'), qt.InputText('', key='lat_input'),
             qt.Text('Lon:', justification='center'), qt.InputText('', key='lat_input'),
             ]
        ]

        return struct

    def main_layout(self):
        import PySimpleGUIQt as qt
        layout = [
            [qt.Frame('', self._localization_frame_(), background_color='#00c2c7'), qt.Frame('', self.weather_api_frame(config=self.config), background_color='#97ebdb')],
            [qt.Frame('', self.geolocale_frame(), background_color='#005582')],
            [qt.Button('Cancel', key='opts_win_cancel'), qt.Button('OK', key='opts_win_ok')]

        ]

        return layout

    def __init__(self, config=None):
        """
        Initialize a new instance of the options window

        :param config: The config object from the App class
        """
        import PySimpleGUIQt as qt
        self.config = config

        self.window = qt.Window('Options', layout=self.main_layout())







