class OptsWindow(object):
    """
    Class containing the information for the Options Window
    """

    def localization_frame(self):
        import PySimpleGUIQt as qt
        frame = [
            [qt.Text('Primary Temperature Unit:', justification='left'),
             qt.Radio('Fahrenheit', group_id='temp_unit', default=True), qt.Radio('Celsius', group_id='temp_unit'),
             qt.Radio('Kelvin', group_id='temp_unit')
             ]
        ]
        return frame

    def main_layout(self):
        import PySimpleGUIQt as qt
        layout = [
            [qt.Frame('', self.localization_frame())],
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







