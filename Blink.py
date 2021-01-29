from machine import Pin # machine is used to interact the device with micro python
import utime # used for the delaying the led

led = Pin(25,Pin.OUT) # Pin 25 is the Output Pin for the internal led on the pico

while True:
    
    led.value(1) # Turns on the led with the value 1
    utime.sleep(2) # Delay of 2 sec
    led.value(0) # Turns off the led with the value 0
    utime.sleep(2) # Delay of 2 sec