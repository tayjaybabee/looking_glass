class LoggerError(Exception):
    """
    Namespace for exceptions exclusive to the set-up and running of the program's logger

    """
    def __init__(self, info=None, logger=None):
        self.message = "There has been an error with the logger helper"
        if info is None:
            info_str = 'No additional information provided. Please see documentation.'
