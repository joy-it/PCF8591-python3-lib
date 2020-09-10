# -*- coding: utf-8 -*-
import smbus
from time import sleep

i2c = smbus.SMBus(1)     # Erzeugen und oeffnen einer I2C-Instanz

def readADCvalue(i2cDeviceAddr, channel):
   value=i2c.read_byte_data (i2cDeviceAddr, channel)  
   sleep (0.01)
   value=i2c.read_byte_data (i2cDeviceAddr, channel)  # aktueller Wert wird ausgelesen
   return value

def readADCvoltage(i2cDeviceAddr, channel):
   value=i2c.read_byte_data (i2cDeviceAddr, channel)  
   sleep (0.01)
   value=i2c.read_byte_data (i2cDeviceAddr, channel)  # aktueller Wert wird ausgelesen
   value= value * (3.3 / 255)                         # Umrechnung in eine Spannung
   return value

def writeADC(i2cDeviceAddr, channel, value):
   i2c.write_byte_data (i2cDeviceAddr, 0x40+channel, value) 
