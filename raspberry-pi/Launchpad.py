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
                for x in range(37): 
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
                                servocounter =+ 6 
                                servo1.angle = servocounter
                                if servocounter < 60: 
                                        redled.value = True 
                                        Counter = 2
                                        print(Counter)

                Counter = 10 
                redled.value = False
                greenled.value = True
                servo1.angle = 180
                print("Launch")
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


                








    