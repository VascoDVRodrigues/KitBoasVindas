from machine import Pin, ADC, PWM
import time
 
ldr = ADC(27)
pwm = PWM(Pin(15))
pwm.freq(1000)

 
#while True:
#     print(ldr.read_u16())
#     time.sleep(.5)
while True:
    for duty in range(65025):
        pwm.duty_u16(duty)
        time.sleep(0.0001)
    for duty in range(65025, 0, -1):
        pwm.duty_u16(duty)
        time.sleep(0.0001)