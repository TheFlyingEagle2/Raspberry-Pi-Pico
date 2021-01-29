from machine import Pin # machine is used to interact the device with micro python
import utime # used for the delaying the led

led = Pin(25,Pin.OUT) # Pin 25 is the Output Pin for the internal led on the pico

while True:
    
    led.toggle() # Turns on and off the led
    utime.sleep(2) # Delay of 2 sec
