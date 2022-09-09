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
Counter = 10
greenled.value = False
redled.value = False 
servo1.angle = 0 
servocounter = 0 

while True: 
        servo1.angle = 0 
        if button.value == True: 
                print("Button Works")
        if button.value == True: 
                time.sleep(1)
                for x in range(10): 
                        Counter -= 1
                        if Counter == 3
                                BeginServo() 
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
        def BeginServo(): 
                print("Servo")
                if servocounter < 60: 
                        servo1.angle = servocounter 
                        servocounter =+ 1 
                if servocounter > 60 and servocounter < 120:  


                








    