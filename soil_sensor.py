from machine import Pin,ADC
from time import sleep
pot=ADC(0)
for i in range(20):
 pot_value=pot.read()
 print(pot_value)
 sleep(3)

