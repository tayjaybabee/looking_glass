class TopMenu:

    def _menu_(self):
        """
        Model for the top menu bar on the top window

        :return: Iterable for PySimpleGUI to turn into a menu layout
        """
        menu = [
            ['File', ['Settings::_SETTINGS_BUTTON_']],
            ['Help', ['Docs', ['@softworks.inspyre.tech'], ], ],
        ]
        return menu

    def __init__(self):
        self.menu = self._menu_()
