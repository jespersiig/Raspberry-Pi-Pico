from machine import Pin
import utime

led = Pin(25, Pin.OUT)

answer = input ("What is your name name? ")
while answer != "Clark Kent":
    print("Nice to meet you, "+answer+" - but you are not Superman.")
    led.value(0)
    for i in range(20):
        led.toggle()
        utime.sleep(0.25)
    answer = input("Next person: What is your name? ")
print("Finally - You are Superman!")
led.value(1)
utime.sleep(5)
led.value(0)
