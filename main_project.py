import network 
import ujson 
import time
import gc 
import urequests as requests 
from machine import Pin,ADC 

moisture_pin=ADC(0)
motora1=Pin(12,Pin.OUT)
motorb1=Pin(13,Pin.OUT)


while True:
 moisture_value=moisture_pin.read()
 ##print(moisture_value)
 time.sleep(1)
 
 
 ##rah andazi be soorate hooshmand va bedoone niaz be internet
 while moisture_value<500:
       motora1.value(1) 
       motorb1.value(0)
         pass
         
         
         

##rah andazi az tarigh internet
def connect():
  ssid = ''
  password =  ''    
 
  s = network.WLAN(network.STA_IF) 
 
  if s.isconnected() == True:
      print("Already connected")
      return
 
  s.active(True)
  s.connect(ssid, password)
  while s.isconnected() == False:
    print("connecting to wifi")
    led.value(0)
    time.sleep(1)
    led.value(1)
    time.sleep(1)
    pass
  print("Connection successful")  
  
url='http://192.168.43.79:8000/delta/tele/led/'
value_list=[300,500,800,1024]
state_list=['waterlogged','dranch','damp','dry']
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
counter=0
while True:
  if button.value() == 0:
    while True:
      led.value(1)
      connect() 
      for m in value_list:
        if moisture_value<=m: 
          state=state_list[counter]
          break
        else:
          counter+=1
      dade={'moisture':moisture_value,'state':state}##dade ke ghast ersal on be server ra darem
      dade_dic=ujson.dumps(dade)      
      send=requests.request('POST', url, data=dade_dic,headers=headers, stream=False)
      x=send.json()
      x=x['state']
      while x=='on':
        motora1.value(1) 
       motorb1.value(0)
      
      send.close()
      counter=0
      gc.collect()
  else: 
    led.value(0)
    ## press flash button to run
    pass







