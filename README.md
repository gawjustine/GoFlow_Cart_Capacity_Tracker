# GoFlow - Cart Density Tracker
This project monitors crowd density inside train cars with YOLOv8 Head Detector and models the fullness of the car 
(measured in percentage) into a graphical user interface that "fills up" as the car fills up. A fully visible train indicates a completely full train.
It also models the fullness onto a series of led lights that turn on according to the percentage as well. All three lights turned on indicates a completely full train.

This project aims to integrate AI image detection, GUI, and visible light indicators to prompt individuals to move to less congested parts of the train.
Highly dense crowds, especially during rush hour, often inhibit movement of passengers on and off the train, as well as place individuals at risk due to limited space
to react in the event of an emergency. 

### Getting Started: Installation & Requirements
#### Software
The following Python libraries should be installed via Windows PowerShell or Terminal for Mac/Linux:  
(sometimes for Mac you will need to use pip3 instead of pip)  

````
pip install opencv-python  
pip install ultralytics
pip install pillow
````
Don't forget to download nano.pt for the YOLO ai! Original owners: https://github.com/Abcfsa/YOLOv8_head_detector  
You may need to set up a virtual environment to run Tkinter especially if you're on Windows.

#### Hardware  
Components used:
1. 3 led lights
2. Breadboard
3. MM jumper cables
4. Raspberry Pi Pico
5. 220 or 330 ohm resistors

You will need to install Thonny and then open the pico_main.py code with it. 
Hold BOOTSEL on your Pico, plug in the USB, and release when you get a confirmation message. 
Then click "Run" on the top menu bar, and "Configure Interpreter". Select "MicroPython (Raspberry Pi Pico)" for the interpreter.
Click "Install or Update MicroPython" and follow the listed instructions to connect your Pico. 
You will then have to download the code onto your Pico. Click "Save as" and select "Raspberry Pi Pico". 
Ensure that you rename your file to ````main.py````, as the Pico will ignore the code otherwise.

_Wiring Diagram: Note the parallel resistor setup used to brighten the LEDs_
![Image](https://github.com/user-attachments/assets/acaacd66-80d2-45ad-b981-70662c52152a)

> [!TIP]
> **Important:** Refer to the Pico datasheet for pinouts. Ensure your LEDs are connected to the correct GP pins as defined in your code.

### Usage
1. Download all files and ensure that all libraries are installed.
2. Setup hardware and configure the serial port to be whichever port you plug your Pico into. For Windows your ports are labelled but for Mac or Linux, type in
   ````ls /dev/cu.usbmodem*```` into Terminal to determine which port your Pico is using. Paste that into the serial port.
3. You can debug your Pico using the ````test_circuit.py```` file if the Pico is connecting but not turning on. Ensure connection is stable and run the file.
   Unplugging and repluggin the Pico typically works when the code is not running.
4. The only file that should be run is the ````main.py```` file.
