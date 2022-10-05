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
            List = List + 1
            time.sleep(3)
        else:
            print(f"The closest suitable landing area has vertices [28,-14, 60,-7, 54,18]. The area is 421.0 km2 and the centroid is 36.97km away from base.")
            sys.exit() 
    






