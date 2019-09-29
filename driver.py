import time
from machine import Pin,ADC

motora1=Pin(12,Pin.OUT)
motorb1=Pin(13,Pin.OUT)

## control az tarigh rotubat khande shode tavasote sensor
sensor_pin=ADC(0)
sensor_value=sensor_pin.read();
while (sensor_value<900):
 motora1.value(1) ##baraye khamoosh kardane dasti bayad meghdar value ra 0 gharar dad
 motorb1.value(0)
 
 
 
 
 ## code haye zire contorol az tarighe zamanbandi 
 """
for i in range(100):
 motora1.value(1) 
 motorb1.value(0)
 time.sleep(3)
 motora1.value(0) 
 motorb1.value(0)
 time.sleep(3)
 """
 
 



