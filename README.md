# Engineering_4_Notebook

&nbsp;

## Table of Contents
* Launch Pad
  * [Launch Pad Part 1](#Launch-Pad-Part-1)
  * [Launch Pad Part 2](#Launch-Pad-Part-2)
  * [Launch Pad Part 3](#Launch-Pad-Part-3)
  * [Launch Pad Part 4](#Launch-Pad-Part-4)
* Crash Avoidance
  * [Crash Avoidance Part 1](#Crash-Avoidance-Part-1) 
  * [Crash Avoidance Part 2](#Crash-Avoidance-Part-2) 
  * [Crash Avoidance Part 3](#Crash-Avoidance-Part-3) 
  * [Crash Avoidance Part 4](#Crash-Avoidance-Part-4) 
* Landing Area
  * [Landing Area Part 1](#Landing-Area-Part-1)
  * [Landing Area Part 2](#Landing-Area-Part-2)
  * [Landing Area Part 3](#Landing-Area-Part-3)
* Morse Code
  * [Morse Code Part 1](#Morse-Code-Part-1)
  * [Morse Code Part 2](#Morse-Code-Part-2)
* Intro to Cad
  * [Intro to Cad 1](#Intro-to-Cad-Part-1)
  * [Intro to Cad 2](#Intro-to-Cad-Part-2)
  * [Intro to Cad 3](#Intro-to-Cad-Part-3)
  * [Intro to Cad 4](#Intro-to-Cad-Part-4)
  * [Intro to Cad 5](#Intro-to-Cad-Part-5)
* FEA Beam Design
  * [FEA Part 1](#FEA-Part-1)
  * [FEA Part 2](#FEA-Part-2)
  * [FEA Part 3](#FEA-Part-3)
* Templates
  * [Pico_Assignment_Template](#Pico_Assignment_Template)
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

[Back To Top](#Table-of-Contents)
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

[Back To Top](#Table-of-Contents)
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

[Back To Top](#Table-of-Contents)
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

[Back To Top](#Table-of-Contents)
&nbsp;

## Crash Avoidance Part 1

### Description

In this assignment we're learning the basics of the MPU6050. It measures its change in accelertaion and rotation using a gyroscope and an accelerometer 

### Evidence 

<img src="images/Crash 1.gif" width="400" height="600" />

### Wiring

[Wiring](https://github.com/bwright70/RasberryPiPico/blob/main/images/Wiring%202.HEIC)

### Code

```
#type: ignore 
import digitalio
import time  
import board 
import adafruit_mpu6050 
import busio 

led = digitalio.DigitalInOut(board.GP28)
led.direction = digitalio.Direction.OUTPUT 
sda_pin = board.GP16
scl_pin = board.GP17
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c) 

while True: 
        x = mpu.acceleration[0] 
        y = mpu.acceleration[1] 
        z = mpu.acceleration[2] 
        if x > 1:
                print(f"X = {x}") 
```

### Reflection

There was no real goal to this assignment, more just learning how to use the accelerometer and f Strings which will prove very useful in the future. I need to remember to set variables values in the while True loop otherwise they won't update. Also to always save my code because otherwise nothing will work. 

&nbsp;

[Back To Top](#Table-of-Contents)
&nbsp;

## Crash Avoidance Part 2

### Description

The goal of this assignment was to incorporate an led into our code by making it turn on when the board tilted too far, and to use a powerboost as a mobile power source so we could walk around with our board. 

### Evidence 

<img src="images/Crash 2.gif" width="400" height="600" />

### Wiring

[Wiring](https://github.com/bwright70/RasberryPiPico/blob/main/images/Wiring%202.HEIC)

### Code

```
#type: ignore 
import digitalio
import time  
import board 
import adafruit_mpu6050 
import busio 

led = digitalio.DigitalInOut(board.GP28)
led.direction = digitalio.Direction.OUTPUT 
sda_pin = board.GP16
scl_pin = board.GP17
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c) 

while True: 
        x = mpu.acceleration[0] 
        y = mpu.acceleration[1] 
        z = mpu.acceleration[2] 
        # When oriented up the Z acceleration will be about 9.81 m/s^2 which is acceleration due to gravity
        # So the code just checks to see if its oriented anything but up and if it is it turns the led on and prints the Z acceleration 
        if z < 1:
                led.value = True
                print(f"Z = {z}") 
        else: 
                led.value = False 
```

### Reflection

The main hiccup with this assignment was just remembering to charge the power boost before hand. Luckily I grabbed one that was already fully charged, but a lot of time could be spent waiting for it. I didn't have to modify my code much at all as I already had a system in place that worked really well for this assignment.  

&nbsp;

[Back To Top](#Table-of-Contents)
&nbsp;

## Crash Avoidance Part 3

### Description

This assignment we're adding an LCD screen into the previous design. It needs to broadcast the X, Y, and Z values onto the screen, and do all the other things. 

### Evidence 

<img src="images/Crash 3.gif" width="400" height="600" />

### Wiring

[Wiring](https://github.com/bwright70/RasberryPiPico/blob/main/images/Wiring%203.HEIC)

### Code

```
#type: ignore 
import digitalio
import time  
import board 
import adafruit_mpu6050 
import busio 
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio
displayio.release_displays() #put this line just below your imports


led = digitalio.DigitalInOut(board.GP28)
led.direction = digitalio.Direction.OUTPUT 
sda_pin = board.GP16
scl_pin = board.GP17
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP15)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

# Accelerometer Address is ['0x68']
# LCD Screen Address is ['0x3d']



while True: 
        xa = round(mpu.acceleration[0], 3) 
        ya = round(mpu.acceleration[1], 3) 
        za = round(mpu.acceleration[2], 3) 
        
        # create the display group
        splash = displayio.Group()

        # add title block to display group
        XAcceleration = (f"X = {xa}")
        # the order of this command is (font, text, text color, and location)
        text_area = label.Label(terminalio.FONT, text=XAcceleration, color=0xFFFF00, x=5, y=5)
        splash.append(text_area)    

        YAcceleration = (f"Y = {ya}")
        text_area = label.Label(terminalio.FONT, text=YAcceleration, color=0xFFFF00, x=5, y=20)
        splash.append(text_area)

        ZAcceleration = (f"Y = {za}")
        text_area = label.Label(terminalio.FONT, text=ZAcceleration, color=0xFFFF00, x=5, y=35)
        splash.append(text_area)

        display.show(splash)  
        if za < 1:
                led.value = True
        else: 
                led.value = False   
```

### Reflection

Personally I did not like this assignment. It involved just copying a bunch of code so that the LCD Screen could work. Because of how the Accelerometer and LCD screen work, they can communicate through the same wire, but to do that you have to figure out the address of each of the things, which involves copying different code. Mainly [this code](https://github.com/bwright70/RasberryPiPico/blob/main/raspberry-pi/I2CAddress) which when run finds the addresses of the two I2C devices. Basically this assignment was a bunch of copying and not very interesting.  

&nbsp;

[Back To Top](#Table-of-Contents)
&nbsp;

## Crash Avoidance Part 4

### Description

This was an optional assignment that incorporates the Altimeter into the previous three assignments. The Altimeter measures altitude through barametric pressure. The goal was to turn on a green led when the altimeter was three meters above its starting point and the red led doesn't turn on when the green led is. 

### Evidence 

<img src="images/Crash 4.gif" width="400" height="600" />

### Wiring

[Wiring](https://github.com/bwright70/RasberryPiPico/blob/main/images/Altimeter%20Wiring.JPG)

### Code

```
#type: ignore 
import digitalio
import time  
import board 
import adafruit_mpu6050 
import busio 
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio
import adafruit_mpl3115a2
displayio.release_displays() #put this line just below your imports


redled = digitalio.DigitalInOut(board.GP28)
redled.direction = digitalio.Direction.OUTPUT 
greenled = digitalio.DigitalInOut(board.GP1)
greenled.direction = digitalio.Direction.OUTPUT 
sda_pin = board.GP16
scl_pin = board.GP17
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP15)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
sensor = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x60)

# Accelerometer Address is ['0x68']
# LCD Screen Address is ['0x3d']
# Altimeter Address is ['0x60']

# This is the altitude when the code first runs and we use it to compare to the constatly updating altitude 
setalt = sensor.altitude 

while True: 
    xa = round(mpu.acceleration[0], 3) 
    ya = round(mpu.acceleration[1], 3) 
    za = round(mpu.acceleration[2], 3) 
    alt = sensor.altitude

    # create the display group
    splash = displayio.Group()
    
    # This checks to see if we're 3 meters above starting altitude
    # If it is then it turns the green light on and updates the LCD Screen like normal 
    if alt > setalt + 3: 
        greenled.value = True 

        redled.value = False

        XAcceleration = (f"X = {xa}")
        text_area = label.Label(terminalio.FONT, text=XAcceleration, color=0xFFFF00, x=5, y=5)
        splash.append(text_area)    

        YAcceleration = (f"Y = {ya}")
        text_area = label.Label(terminalio.FONT, text=YAcceleration, color=0xFFFF00, x=5, y=20)
        splash.append(text_area)

        ZAcceleration = (f"Z = {za}")
        text_area = label.Label(terminalio.FONT, text=ZAcceleration, color=0xFFFF00, x=5, y=35)
        splash.append(text_area)
        display.show(splash)  

        Altitude = (f"A = {alt}")
        text_area = label.Label(terminalio.FONT, text=Altitude, color=0xFFFF00, x=5, y=50)
        splash.append(text_area)
        display.show(splash)  
    # This checks to see if we're below the green light zone
    # If we are AND we've tilted too far in any direction it turns the red warning light on 
    elif za < 1 and alt < setalt + 3:
        print("New")
        redled.value = True

        WARNING = ("WARNING")
        text_area = label.Label(terminalio.FONT, text=WARNING, color=0xFFFF00, x=35, y=35)
        splash.append(text_area)

        display.show(splash)  
    # This is just the normal loop if the other two loops aren't true 
    else: 
        redled.value = False   
        greenled.value = False
        # add title block to display group
        XAcceleration = (f"X = {xa}")
        # the order of this command is (font, text, text color, and location)
        text_area = label.Label(terminalio.FONT, text=XAcceleration, color=0xFFFF00, x=5, y=5)
        splash.append(text_area)    

        YAcceleration = (f"Y = {ya}")
        text_area = label.Label(terminalio.FONT, text=YAcceleration, color=0xFFFF00, x=5, y=20)
        splash.append(text_area)

        ZAcceleration = (f"Z = {za}")
        text_area = label.Label(terminalio.FONT, text=ZAcceleration, color=0xFFFF00, x=5, y=35)
        splash.append(text_area)
        display.show(splash)  

        Altitude = (f"A = {alt}")
        text_area = label.Label(terminalio.FONT, text=Altitude, color=0xFFFF00, x=5, y=50)
        splash.append(text_area)
        display.show(splash)  
```

### Reflection

This assignment came with a lot of unforseen difficultites. The actual coding part wasn't too tricky I just ran the [this code](https://github.com/bwright70/RasberryPiPico/blob/main/raspberry-pi/I2CAddress) and then added and if and if else statements so that the leds would turn on and off at the correct times. The real problem came from my Powercell which we used last assignment as a mobile power source. The Powercell suddenly decided to stop working, and so even though nothing looked wrong, when I plugged the Powercell in the code suddenly stopped working and kept throwing up and error saying that it was missing the address for the accelerometer. Even when I plugged it back into the computer, it still broke. The only way to fix it to comment then uncomment that part of the code. I ended up just stealing someone elses Powercell. The second problem was if else statements (written as elif) Apparently they don't work because even when my if statement was rinning the elif statement was still turning on the red led which isn't supposed to happen. I ended up just writing it like an if statement but left in the elif so that people could see what I intended. Lot of hardware and weird syntax issues, but nothing too crazy. 

&nbsp;

[Back To Top](#Table-of-Contents)
&nbsp;

## Landing Area Part 1

### Description

This assignment throws all the wiring out and has us do actual coding. The goal is to allow a user to input three cordinates in a X,Y format and it spits out the area for a triangle created by those three points. 

### Evidence 

<img src="images/Landing Area 1.gif" width="400" height="600" />

### Code

```
#type: ignore 
import time 

# |(Ax(By - Cy) + Bx(Cy - Ay) + Cx(Ay - By) / 2| 

def FindArea(AX,AY,BX,BY,CX,CY):
        Area = abs((AX * (BY - CY) + BX * (CY - AY) + CX * (AY - BY)) / 2)
        return Area

while True: 
    
    try: 
        print("Type Cordinates in an X,Y Format")
        time.sleep(1)
        cordinate1 = input("Type First Cordinate: ")
        cordinate2 = input("Type Second Cordinate: ")
        cordinate3 = input("Type Third Cordinate: ")
        A = cordinate1.split(",")
        B = cordinate2.split(",")
        C = cordinate3.split(",")
        time.sleep(1)
        AX = float(A[0])
        AY = float(A[1])
        BX = float(B[0])
        BY = float(B[1])
        CX = float(C[0])
        CY = float(C[1])
        print(FindArea(AX,AY,BX,BY,CX,CY))

    except:  
        print("Somethings Wrong")

```

### Reflection

I remember why I don't like coding. We learned how to use the Input() function which waits until the user types something and then saves that info, the Split() function which splits a string into a list, and the Float() function which converts a sting into a float.  

&nbsp;

[Back To Top](#Table-of-Contents)
&nbsp;

## Landing Area Part 2 

### Description

We're adding onto the previous assignment by now having the LCD screen make a graph and display the inputted triangle. 

### Evidence 

<img src="images/Landing Area 2.gif" width="400" height="600" />

### Code

```
#type: ignore 
import digitalio
import time  
import board 
import adafruit_mpu6050 
import busio 
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio
import adafruit_mpl3115a2
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle


displayio.release_displays() #put this line just below your imports


redled = digitalio.DigitalInOut(board.GP28)
redled.direction = digitalio.Direction.OUTPUT 
greenled = digitalio.DigitalInOut(board.GP1)
greenled.direction = digitalio.Direction.OUTPUT 
sda_pin = board.GP16
scl_pin = board.GP17
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP15)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
sensor = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x60)

# Accelerometer Address is ['0x68']
# LCD Screen Address is ['0x3d']
# Altimeter Address is ['0x60']

# |(Ax(By - Cy) + Bx(Cy - Ay) + Cx(Ay - By) / 2| 

def FindArea(AX,AY,BX,BY,CX,CY):
    Area = abs((AX * (BY - CY) + BX * (CY - AY) + CX * (AY - BY)) / 2)
    return Area

def MakeGraph(AX,AY,BX,BY,CX,CY):

    splash = displayio.Group()
    # Make the Line Graph
    vline = Line(64,0,64,64, color=0xFFFF00)
    splash.append(vline)
    hline = Line(0,32,128,32, color=0xFFFF00)
    splash.append(hline)
    # Make Origin
    circle = Circle(64, 32, 1, outline=0xFFFF00)
    splash.append(circle)
    # Triangle 
    triangle = Triangle(int(AX) + 64, 32 - int(AY), int(BX) + 64, 32 - int(BY), int(CX) + 64, 32 - int(CY), outline=0xFFFF00)
    splash.append(triangle)

    display.show(splash) 

while True: 

    try:
        splash = displayio.Group()

        # This allows the LCD screen to turn on 
        #///////////////////////////////////////////////////////////////////////////////////
        Hello = ("hello")
        text_area = label.Label(terminalio.FONT, text=Hello, color=0xFFFF00, x=5, y=5)
        splash.append(text_area) 
        #//////////////////////////////////////////////////////////////////////////////////

        print("Type Cordinates in an X,Y Format")
        time.sleep(1)
        cordinate1 = input("Type First Cordinate: ")
        cordinate2 = input("Type Second Cordinate: ")
        cordinate3 = input("Type Third Cordinate: ")
        A = cordinate1.split(",")
        B = cordinate2.split(",")
        C = cordinate3.split(",")
        time.sleep(1)
        AX = float(A[0])
        AY = float(A[1])
        BX = float(B[0])
        BY = float(B[1])
        CX = float(C[0])
        CY = float(C[1])
        print(f"Area: {FindArea(AX,AY,BX,BY,CX,CY)}")
        MakeGraph(AX,AY,BX,BY,CX,CY) 
        time.sleep(5)
    
    except:
        print("Somethings Wrong")
```

### Reflection

Nothing much new for this assignment. I copied some code that makes a triangle, two lines and a circle. the trickyest thing was the actual corrodinate of the graph. The graph for the Y axis is flipped so what would normally be positive is negative and the origin is actually at 64,32, so I had to ajust the inputted corrodinates so that they matched the origin. This was acomplished by adding 64 to the x values and making the y vaules negative then adding 32 to them. 

&nbsp;

[Back To Top](#Table-of-Contents)
&nbsp;

## Landing Area Part 3

### Description

We're moving away from the user input code, and instead taking a list of corodinates and graphing four triangles. Then finding the center distance and the Area of the closest Triangle with and area greater than 100 and printing that. The Goal of this code is to work no matter how many triangles we have to Graph. 

### Evidence 

<img src="images/Landing Area 2.gif" width="400" height="600" />

### Code

```
#type: ignore 
import digitalio
import time  
import sys
import board 
import adafruit_mpu6050 
import busio 
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio
import adafruit_mpl3115a2
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle


displayio.release_displays() #put this line just below your imports


redled = digitalio.DigitalInOut(board.GP28)
redled.direction = digitalio.Direction.OUTPUT 
greenled = digitalio.DigitalInOut(board.GP1)
greenled.direction = digitalio.Direction.OUTPUT 
sda_pin = board.GP16
scl_pin = board.GP17
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP15)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
sensor = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x60)

# Accelerometer Address is ['0x68']
# LCD Screen Address is ['0x3d']
# Altimeter Address is ['0x60']

# Area of Triangle
# |(Ax(By - Cy) + Bx(Cy - Ay) + Cx(Ay - By) / 2| 
# Center of Triangle
# ((AX+BX+CX)/3, (AY+BY+CY)/3)

def FindArea(AX,AY,BX,BY,CX,CY):
    Area = abs((AX * (BY - CY) + BX * (CY - AY) + CX * (AY - BY)) / 2)
    return Area

def FindCenter(AX,AY,BX,BY,CX,CY): 
   CX = ((AX+BX+CX)/3) 
   CY = ((AY+BY+CY)/3)
   Length = ((CX - 64)**2 + (CY - 32)**2)**0.5
   return Length 

def MakeGraph(AX,AY,BX,BY,CX,CY):

    splash = displayio.Group()

    vline = Line(64,0,64,64, color=0xFFFF00)
    splash.append(vline)
    hline = Line(0,32,128,32, color=0xFFFF00)
    splash.append(hline)
    
    circle = Circle(64, 32, 1, outline=0xFFFF00)
    splash.append(circle)
    
    triangle = Triangle(int(AX) + 64, 32 - int(AY), int(BX) + 64, 32 - int(BY), int(CX) + 64, 32 - int(CY), outline=0xFFFF00)
    splash.append(triangle)

    display.show(splash) 

List = 0 
BestTriangle = 10000000000000

while True: 

        splash = displayio.Group()

        # This allows the LCD screen to turn on 
        #///////////////////////////////////////////////////////////////////////////////////
        Hello = ("hello")
        text_area = label.Label(terminalio.FONT, text=Hello, color=0xFFFF00, x=5, y=5)
        splash.append(text_area) 
        #//////////////////////////////////////////////////////////////////////////////////
        
        Points = [[-50,-17,-57,12,-22,-7],[28,-14,60,-7,54,18],[45,30,51,-1,18,6],[5,5,19,15,22,10]]
        if List < len(Points):
            AX = Points[List][0]
            AY = Points[List][1]
            BX = Points[List][2]
            BY = Points[List][3]
            CX = Points[List][4]
            CY = Points[List][5]
            print(f"SITE {List + 1}:")
            print(f"Area: {FindArea(AX,AY,BX,BY,CX,CY)}km2")                                                                            
            print(f"Center Distance is: {FindCenter(AX,AY,BX,BY,CX,CY)}km") 
            MakeGraph(AX,AY,BX,BY,CX,CY) 
            if FindArea(AX,AY,BX,BY,CX,CY) > 100:
                if FindCenter(AX,AY,BX,BY,CX,CY) < BestTriangle:
                    BestTrangleCenter = FindCenter(AX,AY,BX,BY,CX,CY) 
                    BestTriangleArea = FindArea(AX,AY,BX,BY,CX,CY) 
                    BestTrianglePoints = Points[List]
                    BestTriangleSite = List + 1 

            List = List + 1
            time.sleep(3)
        else:
            print(f"The closest suitable landing area is Site {BestTriangleSite} and has vertices {BestTrianglePoints}. The area is {BestTriangleArea}km2 and the centroid is {BestTrangleCenter}km away from base.")
            sys.exit() 
```

### Reflection

This assignment was not actually that difficult though I did have to restart it because I didn't relize it had to be a loop and was manually entering corodinates. Biggest problems were figuring out how lists work and keeping the Best Triangle saved between loops. Turns out you can just make a massive variable to start out with then set it equal to something in the loop later. 


&nbsp;

[Back To Top](#Table-of-Contents)
&nbsp;

## Morse Code Part 1

### Description

We need to convert an inputted english message into Morse Code 

### Evidence 

<img src="images/Morse Code 1.gif" width="600" height="400" />

### Code

```
#type: ignore 
import time  

MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-', ' ':'/'}

while True:
    Message = input("Type English Message: ")
    if Message == "-q": 
        break
    Message = Message.upper()
    Length = len(Message)
    print(Length)
    time.sleep(3)
    NewMessage = ""
    for Letter in Message:
        Letter = MORSE_CODE[Letter]
        NewMessage = NewMessage + Letter + " "
    print(NewMessage)
```

### Reflection

Turns out you can loop through a string if your range is a string. So you can have a variable that adds to itself and translate into morse code. The directory was cool and I added to it to include spaces in english being "/" in morsecode as that was part of the assignment. This was mainly a logic puzzle that still doesn't fully make sense to me. 

&nbsp;

[Back To Top](#Table-of-Contents)
&nbsp;

## Morse Code Part 2

### Description

We're adding an led that blinks out our morsecode message.  

### Evidence 

<img src="images/Morse Code 2.gif" width="400" height="600" />

### Code

```
#type: ignore 
import digitalio
import time 
import board

greenled = digitalio.DigitalInOut(board.GP16)
greenled.direction = digitalio.Direction.OUTPUT
redled = digitalio.DigitalInOut(board.GP2)
redled.direction = digitalio.Direction.OUTPUT 

MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-', ' ':'/'}

while True:
    Message = input("Type English Message: ")
    if Message == "-q": 
        break
    Message = Message.upper()
    Length = len(Message)
    print(Length)
    time.sleep(3)
    
    modifier = 0.25

    DotTime = 1 * modifier
    DashTime = 3  *modifier
    BetweenTaps = 1 * modifier
    BetweenLetters = 3 * modifier
    BetweenWords = 7 * modifier

    NewMessage = ""
    for Letter in Message:
        Letter = MORSE_CODE[Letter]
        for Symbol in Letter:
            redled.value = True 
            if Symbol == ".": 
                time.sleep(DotTime)
            if Symbol == "-":
                time.sleep(DashTime)
            redled.value = False
            time.sleep(BetweenTaps)
            if Symbol == " ": 
                time.sleep(BetweenLetters)
            if Symbol == "/":
                time.sleep(BetweenWords)
        NewMessage = NewMessage + Letter + " "
        print(NewMessage)
```

### Reflection

This assignment was actually really easy. It took me about 10 minutes and just a few minor modifications like switching the order of if statements to finish it. All I did was add a second for loop that loops through each letter of the message once it's converted to morsecode, then it determines how long to pause based on the symbol. Thats it; Very simple. 

&nbsp;

[Back To Top](#Table-of-Contents)
&nbsp;

## Intro to Cad Part 1

### Assignment Description

This is the First Onshape Assignment. For this assignment we got into teams of two and each worked on a document together. I was student B and had the responcibiliy of making the Spinner. 

### Part Link 

[Link to Document](https://cvilleschools.onshape.com/documents/3aa312c08f145112890ad27c/w/8b2620cc6fde6f2649d3b2f0/e/9ebfc7450031491fc1528048)

### Part Image

<img src="images/Spinner and Prop.png" width="400" height="400" />

### Reflection

In this assignment I learned how to use the helix tool, in context parts studios, and second end position to make the Spinner. I knew how to use most of these tools already but this was the first time we used them in an actual assignment. There were no major issues other than I didn't read the instructions properly the first time and so hadn't used a second end Position for my Extrude. 

&nbsp;

[Back To Top](#Table-of-Contents)
&nbsp;

## Intro to Cad Part 2

### Assignment Description

This is part 2 of the First Onshape Assignment. For this assignment we got into teams of two and each worked on a document together. I was Student B and had the responcibiliy of making the Prop. 

### Part Link 

[Link to Document](https://cvilleschools.onshape.com/documents/3aa312c08f145112890ad27c/w/8b2620cc6fde6f2649d3b2f0/e/9ebfc7450031491fc1528048)

### Part Image

<img src="images/Spinner and Prop (1).png" width="400" height="400" />

### Reflection

This time I had some weird issues with merge extrudes. I accidently made a new part instead of merging it with the old one and so when I tried to hollow it out it broke. Other than that no major issues. The way the prop was made around the spinner was super clever and I need to remember it for the future. 

&nbsp;

[Back To Top](#Table-of-Contents)
&nbsp;

## Intro to Cad Part 3

### Assignment Description

This is part 3 of the First Onshape Assignment. For this assignment we got into teams of two and each worked on a document together. This was the assembly part of the assignment and so me and my partner worked in the assembly to put together the different parts we made 

### Part Link 

[Link to Document](https://cvilleschools.onshape.com/documents/3aa312c08f145112890ad27c/w/8b2620cc6fde6f2649d3b2f0/e/9ebfc7450031491fc1528048)

### Part Image

<img src="images/Pull Copter.png" width="600" height="600" />

### Reflection

Probably the Easiest of all these assignment. We just put the four parts together and added a Rack and Pinion relation. I had already worked with these because of the robot arm last year so it wasn't too much trouble. 

&nbsp;

[Back To Top](#Table-of-Contents)
&nbsp;

## Intro to Cad Part 4

### Assignment Description

This is part 4 of the First Onshape Assignment. For this assignment we got into teams of two and each worked on a document together. For this final section we learned how to version a document and then each made individual edits to the document. I changed the prop to make more aerodynamtic wings

### Part Link 

[Link to Document](https://cvilleschools.onshape.com/documents/3aa312c08f145112890ad27c/w/8b2620cc6fde6f2649d3b2f0/e/9ebfc7450031491fc1528048)

### Part Image

<img src="images/Spinner and Prop (2).png" width="600" height="600" />

### Reflection

We learned what versions are. They're just different branches of a part, so you can interate off a design without changing the main part. I don't like versions mainly because you can't delete a version once you've made it and the UI isn't super intuative. 

&nbsp;

[Back To Top](#Table-of-Contents)
&nbsp;

## FEA Part 1

### Assignment Description

We're making beams to see how much weight they can hold. The restrictions are that there can't be any over hangs, all angles must be greater than 45 degrees, the beam can't weigh more than 13 grams, and the end of the beam had to be at least 180mm away from the other end. 

### Part Link 

[Link to Document](https://cvilleschools.onshape.com/documents/b0642ff49d8db9b862992a16/w/256263874c5873489822cbff/e/eb74407b2954334966743e40?renderMode=0&uiState=636d0f1d37b6be47af1f6439)

### Part Image

<img src="images/Beam Design 1.png" width="600" height="600" />

### Reflection

Me and my partner went for a triangle heavy design. we added triangles to the walls and a lattice to the floor. We also wanted as close to a roof as possible but extruding everything up added too much weight, so we added triangles to it as well. The goal was for the interior to renforce the exterior at it's stress points and vice versa. 

&nbsp;

[Back To Top](#Table-of-Contents)
&nbsp;

## FEA Part 2

### Assignment Description

We get to learn about how to use an onshape simulation. It shows the displacement and stress points of our design. We just download the sti and then drop it into the website and it does it all for us. 

### Part Image

<img src="images/Beam Simulation.png" width="800" height="300" />

### Reflection

Unfortunently our simulation was kinda broken. The displacement was very broken cause we had to turn off some settings so that the website would work. It ended up misleading us as to how effective our design actually was. 

&nbsp;

[Back To Top](#Table-of-Contents)
&nbsp;

## FEA Part 3

### Assignment Description

We're redesigning based off the simulation. Checking stress points and adding renforcements where nessisary. 

### Part Link 

[Link to Document](https://cvilleschools.onshape.com/documents/b0642ff49d8db9b862992a16/w/256263874c5873489822cbff/e/eb74407b2954334966743e40?renderMode=0&uiState=636d0f1d37b6be47af1f6439)

### Part Image

<img src="images/Beam Design 2.png" width="600" height="600" />

### Reflection

Our biggest stress points were the outside trianges. We added a few extra supports to help it not break. When we ran the simulation again it said everything was perfectly fine. 

&nbsp;

[Back To Top](#Table-of-Contents)
&nbsp;

## Pico_Assignment_Template

### Description


### Evidence 


### Wiring


### Code


### Reflection



&nbsp;

[Back To Top](#Table-of-Contents)
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

[Back To Top](#Table-of-Contents)
&nbsp;
