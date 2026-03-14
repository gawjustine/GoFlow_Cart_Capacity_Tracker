import machine
import sys
import uselect

# Setup LEDs on GPIO 2, 7, 13
leds = [machine.Pin(2, machine.Pin.OUT),
        machine.Pin(7, machine.Pin.OUT),
        machine.Pin(13, machine.Pin.OUT)]

def update_leds(n):
    for i in range(3):
        leds[i].value(1 if i < n else 0)

# Create a 'poll' object to check for incoming data without freezing the Pico
poll_obj = uselect.poll()
poll_obj.register(sys.stdin, uselect.POLLIN)

while True:
    # Check if there is data waiting (wait for 100ms)
    if poll_obj.poll(100):
        # Read the character sent from the PC
        char = sys.stdin.read(1)
        
        if char.isdigit():
            update_leds(int(char))
