from machine import Pin
import utime

led = Pin(25, Pin.OUT)

while True:
    for i in range(3):
            utime.sleep(0.25)
            led.value(1)
            utime.sleep(0.25)
            led.value(0)
    for i in range(3):
            utime.sleep(0.75)
            led.value(1)
            utime.sleep(0.75)
            led.value(0)
    for i in range(3):
            utime.sleep(0.25)
            led.value(1)
            utime.sleep(0.25)
            led.value(0)
    utime.sleep(3)