class TopWindow(object):
    """
        Define a kind of template object to construct windows on later
    """

    def pop_set_win(self, config):
        import PySimpleGUIQt as qt
        from .opts_window import OptsWindow
        win_builder = OptsWindow()
        opts_window = win_builder.window

        while True:
            event, value = opts_window.read(timeout=100)
            if event is None or event == 'opts_win_cancel':
                opts_window.close()
                break

            if event == 'opts_win_ok':
                from lib.common.conf.config import Config
                Config.write('conf/config.ini')

    def first_time(self, config):
        import PySimpleGUIQt as qt
        from icons.app_icons import config_icon
        icon = config_icon()
        message = "It seems that you haven't gone through setting your options yet. Would you like me to open " \
                  "the options window immediately after starting this one time to initialize your config file?"
        query = qt.PopupYesNo(message, title='Config warning...', keep_on_top=True, icon=icon, location=(475, 325))
        if str(query).lower() == 'yes':
            self.pop_set_win(config)

    def top_menu(self):
        menu = [
            ['File', ['Settings::_SETTINGS_BUTTON_']],
            ['Help', ['Docs', ['@softworks.inspyre.tech'],],],
        ]
        return menu

    def button_frame(self):
        """
        Create a frame for our buttons at the bottom of the window

        :returns: Button frame object
        :rtype:
        """
        import PySimpleGUIQt as qt
        b_frame = [
            [qt.Button('Make Another', key='dupe'), qt.Button('Exit', key='top_win_exit')]
        ]
        return b_frame

    def layout(self):
        device_name = 'Living Room'
        import PySimpleGUIQt as qt
        from lib.sense.test import get_temp, get_humidity
        struct = [
            [qt.Menu(self.top_menu())],
            [qt.Text('Welcome to Test API!')],
            [qt.Text(f'Current Interior Temperature in {device_name}'), qt.InputText(get_temp(), key='test_field')],
            [qt.Text(f'Current humidity in {device_name}'), qt.InputText(get_humidity(), key='humidity_results')],
            [qt.Frame('', self.button_frame())]
        ]

        return struct

    def __init__(self, file=None, config=None):
        conf = config
        import PySimpleGUIQt as qt
        grab = conf.get("gui_settings", "grab_anywhere")
        if grab == 'None':
            self.first_time(config)


        self.window = qt.Window('Test win', layout=self.layout(), grab_anywhere=grab)
