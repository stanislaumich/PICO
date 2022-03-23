from machine import Pin
import time
led = Pin(25, Pin.OUT)
while True:
    led.value(1)
    # Ждём 1 секунду
    time.sleep(1)
    # Гасим светодиод
    led.value(0)
    # Ждём 1 секунду
    time.sleep(1)

