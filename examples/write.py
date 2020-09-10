import PCF8591
from time import sleep

adc = PCF8591
i2cAddress = 0x48          # I2C-Adresse des ADCs
CH0 = 0x00  # Channel 0
CH1 = 0x01  # Channel 1
CH2 = 0x02  # Channel 2
CH3 = 0x03  # Channel 3
Out = 0x04  # Output

while True:
  i= 0
  for i in range (255):
    adc.writeADC(i2cAddress, Out, i)
    print (i)
    sleep (0.1)