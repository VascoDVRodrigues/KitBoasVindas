from machine import Pin, ADC
from time import sleep
 
solar = ADC(Pin(27, Pin.IN))
 
while True:
    value = solar.read_u16()
    print(value)
    sleep(.5)
