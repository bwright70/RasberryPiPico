# type: ignore
import board
import digitalio
import time 

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True: 
    led.value = True
    time.sleep(2)
    led.value = False
    time.sleep(2) 
