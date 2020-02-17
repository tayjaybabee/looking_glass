


def _identify_(name, root=False, root_part=None):
    from lib.common.logger import NonsensicalIDRequestError

    """
    Create a module/class-specific logger


    :param name: String - The name you want your logger to be under
    :param root: Boolean - (
                            True = Indentifies caller as top of logger heirarchy

                            NOTE: If providing a value of True to the 'root' argument, whatever is loaded into the
                                  'name' parameter is (for all intents-and-purposes) completely ignored. Therefore, one
                                  could call this function as follows:

                                      log_name = identify('', root=True)

                            False = (or left ignored, which defaults to False) Caller is child

                            NOTE: If you fail to provide a non-empty string while also leaving (or specifying) the
                                  'root' parameter as False
                            )
    :return:
    :raises: NonsensicalIDRequestError
    """



def identify(name, root=False, root_part=None):
    from lib.common.logger import NonsensicalIDRequestError
    try:
        _identify_(name, root=root, root_part=root_part)
    except NonsensicalIDRequestError as e:
        raise

