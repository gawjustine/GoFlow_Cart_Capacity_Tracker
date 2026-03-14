# GenAi_Go_Train_Tracker

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
Ensure that you rename your file to main.py, as the Pico will ignore the code otherwise.

### 
