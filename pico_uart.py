import serial
import time

# this function lets you take in a number from 0 to 100
# then it translates that into 0, 1, 2, 3
def pico_led(input, pico):
    if input < 1:
        set_pico_lights("0", pico)
    elif input > 67:
        set_pico_lights("3", pico)
    elif input > 34:
        set_pico_lights("2", pico)
    elif input >= 1:
        set_pico_lights("1", pico) 

def set_pico_lights(number, pico):
    pico.write(number.encode()) # Send the number as bytes
    print(f"Sent command: {number} lights")





