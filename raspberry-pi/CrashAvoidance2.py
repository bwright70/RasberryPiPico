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
        # So the code just checks to see if its oriented anything but up 
        # If it is it turns the led on and prints the Z acceleration 
        if z < 1:
                led.value = True
                print(f"Z = {z}") 
        else: 
                led.value = False 