# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Raspberry_Pi_Assignment_Template](#Raspberry_Pi_Assignment_Template)
* [Onshape_Assignment_Template](#Onshape_Assignment_Template)

&nbsp;

## Launch Pad Part 1 

### Description

The goal was to get a make a count down when you ran the code. The Countdown started at 10 and went to zero. Once it hit Zero it would stop counting and print "Launch 

### Evidence 



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

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Launch Pad Part 2 

### Description

Now We add in an Led to the previous assignment. A Red led blinks with the countdown and a green led turns on at launch 

### Evidence 

Pictures / Gifs of your work should go here. You need to communicate what your thing does. 

### Wiring

This may not be applicable to all assignments. Anything where you wire something up, include the wiring diagram here. The diagram should be clear enough that I can recreate the wiring from scratch. 

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

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Launch Pad Part 3 

### Description

We continue to build on the previous two assignments now with the introduction of a button. The Code should run until you press the button, and for extra spicy points the code should stop running if the button is pressed again 

### Evidence 

Pictures / Gifs of your work should go here. You need to communicate what your thing does. 
### Wiring

This may not be applicable to all assignments. Anything where you wire something up, include the wiring diagram here. The diagram should be clear enough that I can recreate the wiring from scratch. 

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

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Launch Pad Part 4 

### Description

The final assignment is adding a servo that spins from 0 - 180 at launch. For extra spicy points you can make the servo start spinning at three seconds and end at 180 by launch 

### Evidence 

Pictures / Gifs of your work should go here. You need to communicate what your thing does. 

### Wiring

This may not be applicable to all assignments. Anything where you wire something up, include the wiring diagram here. The diagram should be clear enough that I can recreate the wiring from scratch. 

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

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Raspberry_Pi_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Evidence 

Pictures / Gifs of your work should go here. You need to communicate what your thing does. 

### Wiring

This may not be applicable to all assignments. Anything where you wire something up, include the wiring diagram here. The diagram should be clear enough that I can recreate the wiring from scratch. 

### Code
Give me a link to your code. [Something like this](https://github.com/millerm22/Engineering_4_Notebook/blob/main/Raspberry_Pi/hello_world.py). Don't make me hunt through your folders, give me a nice link to click to take me there! Remember to **COMMENT YOUR CODE** if you want full credit. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

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
