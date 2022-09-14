# type: ignore
import board
import digitalio
import time 

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
Counter = 10 

while True: 
    if Counter > 0: 
        Counter -= Counter 
        led.value = True
        print(Counter)
        time.sleep(2)
        led.value = False
        time.sleep(2)



