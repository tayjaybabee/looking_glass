root_name = str()
logger_started = False


class GUI(object):
    """
    A class that serves as a parent to each window/menu/pop-up class
    """

    def get_logger(self, is_root=False):
        import logging
        global logger_started
        if is_root:
            name = root_name
            logger_started = True
        else:
            name = str(f"{root_name}.{self.name}")
            self.logger_started = True
        log = logging.getLogger(name)
        log.debug(f'Logger started for {name}')
        return log

    def __init__(self, config):
        import PySimpleGUI as psg
        # Todo:
        #    - Find a way to only load the PSG needed
        import PySimpleGUIQt as qt
        from .window_models.opts_window import OptsWindow


        # Give the GUI frameworks easily accessible names
        self.qt = qt
        self.psg = psg
        self.opts_win_active = False
        print(dir(self))

        root_name = str(f'LookingGlass.App.{self.__class__.__name__}')

        parent_log = self.get_logger(is_root=True)

    @staticmethod
    def psg():
        """
        This will give sub-classes access to the PySimpleGUI library

        :return:
        """

        import PySimpleGUI as psg
        return psg

    @staticmethod
    def parent_name():
        return root_name

    @staticmethod
    def top_window(config):
        from .window_models.top_window import TopWindow

        builder = TopWindow(config)

        return builder.window

    @staticmethod
    def options_window(config):
        from .window_models.opts_window import OptsWindow
        import PySimpleGUIQt as qt

        win = OptsWindow(config)

        win = qt.Window('LookingGlass Options', text_justification='center', location=(0, 0), layout=win.main_layout())
        return win
