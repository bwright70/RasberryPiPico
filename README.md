# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Launch Pad Part 1](#LaunchPadPart1)
* [Launch Pad Part 2](#LaunchPadPart2)
* [Launch Pad Part 3](#LaunchPadPart3)
* [Launch Pad Part 4](#LaunchPadPart4)
* [Onshape_Assignment_Template](#Onshape_Assignment_Template)

&nbsp;

## Launch Pad Part 1 

### Description

The goal was to get a make a count down when you ran the code. The Countdown started at 10 and went to zero. Once it hit Zero it would stop counting and print "Launch 

### Evidence 

<img src="images/Launch 1.gif" width="400" height="600" />

### Code

```
# type: ignore
import digitalio
import time 

redled = digitalio.DigitalInOut(board.GP16)
redled.direction = digitalio.Direction.OUTPUT
greenled = digitalio.DigitalInOut(board.GP2)
greenled.direction = digitalio.Direction.OUTPUT
Counter = 10

# Loops 10 times
for x in range(10): 
        Counter -= 1
        redled.value = True
        print(Counter)
        time.sleep(1)
        redled.value = False
        time.sleep(1)
# After turns green led on and prints "Launch"
redled.value = False
greenled.value = True
print("Launch")
```

### Reflection

Intially I used an if statement for this code instead of a for loop. I'm only sharing the final version of my doe because I switched to using a for loop later cause it makes everything else like leds and servos much easier. I also did two assignments at once which wasn't super hard but definently could have been tricky if I had tried to work the button in there as well. In general good to do one thing at a time. 

&nbsp;

## Launch Pad Part 2 

### Description

Now We add in an Led to the previous assignment. A Red led blinks with the countdown and a green led turns on at launch 

### Evidence 

<img src="images/Launch 1.gif" width="400" height="600" />

### Wiring

[Wiring](https://github.com/bwright70/RasberryPiPico/blob/47ebe8cb5ab559193084ec46f2547a5bf985e203/images/Wiring%201.HEIC)

### Code

```
# type: ignore
import digitalio
import time 

redled = digitalio.DigitalInOut(board.GP16)
redled.direction = digitalio.Direction.OUTPUT
greenled = digitalio.DigitalInOut(board.GP2)
greenled.direction = digitalio.Direction.OUTPUT
Counter = 10

# Loops 10 times
for x in range(10): 
        Counter -= 1
        redled.value = True
        print(Counter)
        time.sleep(1)
        redled.value = False
        time.sleep(1)
# After turns green led on and prints "Launch"
redled.value = False
greenled.value = True
print("Launch")
```
Same code as before cause I did both assignments at once 

### Reflection

This is the exact same as the last assignment cause I did them at the same time. Not difficult but the wiring could be better. Also my syntax for variables could be better. I personally prefer the capatlize every word method but I was lazy and didn't do that so future variables look weird. redled should be RedLed. 

&nbsp;

## Launch Pad Part 3 

### Description

We continue to build on the previous two assignments now with the introduction of a button. The Code should run until you press the button, and for extra spicy points the code should stop running if the button is pressed again 

### Evidence 

<img src="images/Launch 3.gif" width="400" height="600" />

### Wiring

[Wiring](https://github.com/bwright70/RasberryPiPico/blob/47ebe8cb5ab559193084ec46f2547a5bf985e203/images/Wiring%201.HEIC)

### Code

```
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
        # Testing to make sure button works 
        if button.value == True: 
                print("Button Works")
        if button.value == True: 
                # Pause so it doesn't accidently immidetly abort 
                time.sleep(1)
                for x in range(10): 
                        Counter -= 1
                        redled.value = True
                        print(Counter)
                        # Checks between sleeps so that no matter when you press the button it will work 
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
        # Abort function that resets code 
        def Abort(): 
                print("ABORT") 
                sys.exit("ABORT") 
```

### Reflection

When I was first wiring the button I wired it into ground and 3v and every single time I pressed the button it short circuited my board. Not a major problem because it didn't deal any damage to my board, but defiently not a good idea. Getting the Abort() function working was tricky, but I figured out that If I put a check between each of the time.sleeps, no matter when I pressed the button, it would Abort. 

&nbsp;

## Launch Pad Part 4 

### Description

The final assignment is adding a servo that spins from 0 - 180 at launch. For extra spicy points you can make the servo start spinning at three seconds and end at 180 by launch 

### Evidence 

<img src="images/Launch 4.gif" width="400" height="600" />

### Wiring

[Wiring](https://github.com/bwright70/RasberryPiPico/blob/47ebe8cb5ab559193084ec46f2547a5bf985e203/images/Wiring%201.HEIC)

### Code
```
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
```

### Reflection

The spicy section of this assignment was really tricky. My main problem was that while a time.sleep was active I couldn't do anything else, and so the pauses I had to make the countdown and flashing leds work was prohibitting the servo from running. Using my current method the servo would stop and start with the leds which wasn't what I wanted. So I redid alot of my code and ended up using the rate at which the computer processesc the code as a timer. Each loop of the for loop without interuptions is 0.033 seconds. 90 Loops adds to seconds and the other 7 are for the first 7 seconds. It definently a janky stupid method, but it does work. 

&nbsp;

## Crash Avoidance Part 1

### Description

In this assignment we're learning the basics of the MPU6050. It measures its change in accelertaion and rotation using a gyroscope and an accelerometer 

### Evidence 


### Wiring


### Code


### Reflection


&nbsp;

## Crash Avoidance Part 2

### Description


### Evidence 


### Wiring


### Code


### Reflection


&nbsp;

## Crash Avoidance Part 3

### Description


### Evidence 


### Wiring


### Code


### Reflection


&nbsp;


## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;
