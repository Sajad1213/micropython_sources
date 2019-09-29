from machine import Pin,Timer,PWM
pwm = PWM(Pin(12),100) #create PWM object from a pin, and set frequency
polar = 0            
duty = 0             

def setLed(t):        #create a variable, and change it between 0 and 1008
  global duty,polar
  if(polar == 0):
    duty+=16
    if(duty >= 1008):
      polar = 1
  else:
    duty -= 16
    if(duty <= 0):
      polar = 0
  pwm.duty(duty)      #set duty of the PWM pin2(to control led brightness

tim = Timer(1)        #create Timer object from Virtual timers with timer ID=1
tim.init(period=10,mode=Timer.PERIODIC, callback=setLed) #keeping breathLight function for 10ms. 

#Catch exceptions,stop program if interrupted accidentally in the 'try'
try:                     
  while True:
    pass
except:                #Capture anomaly, deinit Timer and PWM
  tim.deinit()
  pwm.deinit()
