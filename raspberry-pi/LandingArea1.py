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


try: 

    cordinate1 = input("Type First Cordinate")


except:  
    pass




