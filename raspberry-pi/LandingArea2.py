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






