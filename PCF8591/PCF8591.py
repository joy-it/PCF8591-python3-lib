# -*- coding: utf-8 -*-
import smbus
from time import sleep

i2c = smbus.SMBus(1)     

def readADCvalue(i2cDeviceAddr, channel):
   value=i2c.read_byte_data (i2cDeviceAddr, channel)  
   sleep (0.01)
   value=i2c.read_byte_data (i2cDeviceAddr, channel)  # read current analog value
   return value

def readADCvoltage(i2cDeviceAddr, channel):
   value=i2c.read_byte_data (i2cDeviceAddr, channel)  
   sleep (0.01)
   value=i2c.read_byte_data (i2cDeviceAddr, channel)  # read current analog value
   value= value * (3.3 / 255)                         # conversion to a voltage
   return value

def writeADC(i2cDeviceAddr, channel, value):
   i2c.write_byte_data (i2cDeviceAddr, 0x40+channel, value) # write a value to the ADC output
