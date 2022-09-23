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

setalt = sensor.altitude 

while True: 
    xa = round(mpu.acceleration[0], 3) 
    ya = round(mpu.acceleration[1], 3) 
    za = round(mpu.acceleration[2], 3) 
    alt = sensor.altitude

    # create the display group
    splash = displayio.Group()
    
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
    elif za < 1:
        redled.value = True

        WARNING = ("WARNING")
        text_area = label.Label(terminalio.FONT, text=WARNING, color=0xFFFF00, x=35, y=35)
        splash.append(text_area)

        display.show(splash)  
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


