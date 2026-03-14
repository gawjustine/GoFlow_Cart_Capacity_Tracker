from train_gui import root, update_from_count, count_to_percent
from camcounter import get_count, cleanup
from pico_uart import pico_led
import serial
import time

SERIAL_PORT = '/dev/cu.usbmodem1101'
BAUD_RATE = 115200
UPDATE_INTERVAL = 100

try:
    pico = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print(f"Connected to Pico on {SERIAL_PORT}")
    time.sleep(2)
except serial.SerialException as e:
    print(f"Error: Could not open port {SERIAL_PORT}.")
    print("Make sure Thonny is closed and the Pico is plugged in!")

#change time as req for freq of taking frames

def loop():
    count = get_count()
    update_from_count(count)
    percent = count_to_percent(count)
    pico_led(percent, pico)
    root.after(UPDATE_INTERVAL, loop)

def close_app():
    cleanup()
    root.destroy()
    if 'pico' in locals() and pico.is_open:
        pico.close()
        print("Connection closed.")

root.bind("q", lambda e: close_app())
root.protocol("WM_DELETE_WINDOW", close_app)

loop()
root.mainloop()
