import PCF8591
from time import sleep

adc = PCF8591
i2cAddress = 0x48           # ADC I2C-Address
CH0 = 0x40  # Channel 0
CH1 = 0x41  # Channel 1
CH2 = 0x42  # Channel 2
CH3 = 0x43  # Channel 3

while True:

  print("CH0-Value: " + str (adc.readADCvalue(i2cAddress, CH0)))
  print("CH0-Voltage: " + str (adc.readADCvoltage(i2cAddress, CH0)) + "V")
  print("CH1-Value: " + str (adc.readADCvalue(i2cAddress, CH1)))
  print("CH1-Voltage: " + str (adc.readADCvoltage(i2cAddress, CH1)) + "V")
  print("CH2-Value: " + str (adc.readADCvalue(i2cAddress, CH2)))
  print("CH2-Voltage: " + str (adc.readADCvoltage(i2cAddress, CH2)) + "V")
  print("CH3-Value: " + str (adc.readADCvalue(i2cAddress, CH3)))
  print("CH3-Voltage: " + str (adc.readADCvoltage(i2cAddress, CH3)) + "V")
  print ("-----------------------------------------------------")
  sleep (1)
  
