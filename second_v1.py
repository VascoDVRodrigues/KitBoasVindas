from machine import Pin, PWM
from time import sleep

led=Pin(15,Pin.OUT)
pwm = PWM(led)
pwm.freq(1000)

while True:
    value = input('Insere um valor entre 0 e 100.\n')
    value = float(value)/100*65025
    value = int(value)
    print(value)
    
    pwm.duty_u16(value)
    sleep(0.01)