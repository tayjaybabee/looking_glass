#!/usr/bin/env python3

def no_device_for_fetch():
    import PySimpleGUI as gui
    _msg = 'You can\'t fetch data from this device option.'
    _popup = gui.PopupOK(_msg, title='No Device to Fetch From')
    if _popup.lower() == 'ok':
        return True
    else:
        return False
