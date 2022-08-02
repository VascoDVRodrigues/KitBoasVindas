from machine import Pin, PWM
from time import sleep

led=Pin(15,Pin.OUT)
pwm = PWM(led)
pwm.freq(1000)

while True:
    for duty in range(65025):
        pwm.duty_u16(duty)
        sleep(0.0001)