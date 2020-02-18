class Application:
    """
    Main class/entry point for LookingGlass whether you're trying to use the GUI or not.

    """

    def __init__(self):
        from argparse import ArgumentParser              # <- To parse cli-arguments

        # Initialize our parser and give our app a description
        parser = ArgumentParser(prog='LookingGlass',
                                usage='%(prog)s [options]',
                                description='LookingGlass gives you a detailed granular look at your home or office\'s'
                                            ' internal climate while also monitoring localized weather-data. Combine '
                                            'LookingGlass with your Smart Thermostat and other devices and it will use '
                                            'collected data to assist you with cost management, maintaining your '
                                            'comfort, so all you have to focus on is what Inspyres you.',
                                prefix_chars='`-',
                                epilog='Inspyre Softworks. run.Everything',
                                allow_abbrev=True
                                )

        # Add some arguments for use in our CLI interface
        parser.add_argument('-v', '--verbose')

        args = parser.parse_args()
        print(args)



        from lib.common.logger.caller import identify    # <- To ensure a properly formatted logger label/name
        from lib.common.logger import start              # <- Need a logger, and don't wanna disobey D.R.Y.
        import LookingGlass as LookingGlass              # <- Import the actual main script

        # Get a logger-friendly name and then pass that name to the logger.start() method
        log_name = identify('', root=True, root_part=None)
        log = start(log_name)




        # Initialize an instance of LookingGlass
        LookingGlass.App()





Application()
