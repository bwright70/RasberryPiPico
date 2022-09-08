# type: ignore
import board
import digitalio
import time 

redled = digitalio.DigitalInOut(board.GP16)
redled.direction = digitalio.Direction.OUTPUT
greenled = digitalio.DigitalInOut(board.GP2)
greenled.direction = digitalio.Direction.OUTPUT
Counter = 10

for x in range(10): 
        Counter -= 1
        redled.value = True
        print(Counter)
        time.sleep(1)
        redled.value = False
        time.sleep(1)
redled.value = False
greenled.value = True
print("Launch")



    