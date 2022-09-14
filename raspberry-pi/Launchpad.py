# type: ignore
import board
import digitalio
import time 
import sys
import pwmio
from adafruit_motor import servo

# This is just set up so that I can use variables instead of typing "digitalio" every time 
redled = digitalio.DigitalInOut(board.GP16)
redled.direction = digitalio.Direction.OUTPUT
greenled = digitalio.DigitalInOut(board.GP2)
greenled.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP15)
button.pull = digitalio.Pull.DOWN
button.direction = digitalio.Direction.INPUT   
pwm_servo = pwmio.PWMOut(board.GP0, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)
greenled.value = False
redled.value = False 
servocounter = 0 

while True: 
        # I reset some values at the start so nothing breaks 
        Counter = 10
        servocounter = 0 
        servo1.angle = servocounter 
        if button.value == True: 
                print("Button Works")
        if button.value == True: 
                # Pause so it doesn't Abort() immediatly 
                time.sleep(1)
                # The 97 times will make sense later
                # Essentially I'm using the the amount of times the computer can run a code as a Timer
                # The first 7 are for the first 7 seconds and the 90 is for the other 3 seconds 
                for x in range(97): 
                        if Counter > 3:
                                Counter -= 1
                                print(Counter)
                                redled.value = True
                                # Abort is a Function that ends my code
                                # I have it check for the button being pressed again every section so that pressing the button at different times doesn't break it 
                                if button.value == True: 
                                        Abort() 
                                time.sleep(0.5)
                                redled.value = False
                                if button.value == True: 
                                        Abort() 
                                time.sleep(0.5)
                        else: 
                                # This is the janky part of the code
                                # Once the Counter is 3 the servo counter ticks up in increments of 2 
                                # The if statements check for certain angles of the servo and do things when the its true 
                                if servocounter == 0: 
                                        redled.value = True 
                                        Counter = 2
                                        print(Counter)
                                if servocounter == 44:
                                        redled.value = False 
                                if servocounter == 90:
                                        redled.value = True  
                                        Counter = 1
                                        print(Counter)
                                if servocounter == 134:
                                        redled.value = False  
                                if servocounter == 178:
                                        greenled.value = True
                                        print("Launch") 
                                servocounter = servocounter + 2
                                servo1.angle = servocounter
                # This is just a reset so the green led doesn't stay on 
                time.sleep(3)
                greenled.value = False 
                servo1.angle = 0
        # Abort function 
        # Flashes a light then restarts 
        def Abort(): 
                print("ABORT") 
                for x in range(10):
                        redled.value = True 
                        time.sleep(0.1)
                        redled.value = False 
                        time.sleep(0.1)
                sys.exit("ABORT") 


                








    