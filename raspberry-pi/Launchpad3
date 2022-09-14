# type: ignore
import board
import digitalio
import time 
import sys

redled = digitalio.DigitalInOut(board.GP16)
redled.direction = digitalio.Direction.OUTPUT
greenled = digitalio.DigitalInOut(board.GP2)
greenled.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP15)
button.pull = digitalio.Pull.DOWN
button.direction = digitalio.Direction.INPUT   
Counter = 10
greenled.value = False
redled.value = False 

while True: 
        if button.value == True: 
                print("Button Works")
        if button.value == True: 
                time.sleep(1)
                for x in range(10): 
                        Counter -= 1
                        redled.value = True
                        print(Counter)
                        if button.value == True: 
                                Abort() 
                        time.sleep(0.5)
                        redled.value = False
                        if button.value == True: 
                                Abort() 
                        time.sleep(0.5)
                        if button.value == True: 
                                Abort() 
                Counter = 10 
                redled.value = False
                greenled.value = True
                print("Launch")
                time.sleep(3)
                greenled.value = False 
        def Abort(): 
                print("ABORT") 
                sys.exit("ABORT") 