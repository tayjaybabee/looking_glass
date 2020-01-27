def convert_temp(temp):
    f = (temp * 9/5) + 32
    return f


def get_temp():
    from sense_emu import SenseHat
    sense = SenseHat()
    sense.show_message('Being accessed by user!')
    print(f"The temperature is {sense.temp}")
    return convert_temp(sense.temp)

def get_humidity():
    from sense_emu import SenseHat
    sense = SenseHat()
    sense.show_message('Getting Humidity')
    return sense.humidity
