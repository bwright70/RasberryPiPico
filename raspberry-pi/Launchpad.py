# type: ignore
import board
import digitalio
import time 
import sys
import pwmio
from adafruit_motor import servo


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
        Counter = 10
        servocounter = 0 
        servo1.angle = servocounter 
        if button.value == True: 
                print("Button Works")
        if button.value == True: 
                time.sleep(1)
                for x in range(97): 
                        if Counter > 3:
                                Counter -= 1
                                print(Counter)
                                redled.value = True
                                if button.value == True: 
                                        Abort() 
                                time.sleep(0.5)
                                redled.value = False
                                if button.value == True: 
                                        Abort() 
                                time.sleep(0.5)
                        else: 
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
                time.sleep(3)
                greenled.value = False 
                servo1.angle = 0
        def Abort(): 
                print("ABORT") 
                for x in range(10):
                        redled.value = True 
                        time.sleep(0.1)
                        redled.value = False 
                        time.sleep(0.1)
                sys.exit("ABORT") 


                








    