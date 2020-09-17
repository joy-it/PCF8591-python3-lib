import PCF8591
from time import sleep

adc = PCF8591
i2cAddress = 0x48          # ADC I²C-Address
Out = 0x04  # Output

while True:
  i= 0
  for i in range (255):
    adc.writeADC(i2cAddress, Out, i)
    print (i)
    sleep (0.1)
