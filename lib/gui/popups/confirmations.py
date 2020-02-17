#!/usr/bin/env python3
import PySimpleGUI as gui


def exit_wo_save():
    """
    GUI Popup to Confirm User Exit w/o Save

    This function will create a popup window asking the user if they are sure they want to exit without saving. After
    the user answers the function will return with a boolean idicating whether the user said Yes (True) or No (False)

    Example:

        confirms = lib.gui.popups.confirmations

        #...

        if confirms.exit_wo_save():
            # Exit, without saving
        else:
            # Most likely return, changing nothing....


    :return: Boolean
    """
    _message = str('Are you sure you want to exit without saving?')

    _popup = gui.PopupYesNo(_message, title='Exit Without Saving')

    if _popup.lower() == 'yes':
        return True
    else:
        return False


