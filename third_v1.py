from machine import Pin, ADC
from time import sleep
 
solar = ADC(Pin(27, Pin.IN))
 
while True:
    value = solar.read_u16()
    light_percentage = value/65535.0 * 100
    light_percentage = round(light_percentage,2)
    print(light_percentage)
    sleep(.5)
