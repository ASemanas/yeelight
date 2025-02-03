#!./.pyenv/versions/3.13.1/bin/python

import sys,yeelight,socket
from yeelight import Bulb,LightType,BulbType,flows,Flow,RGBTransition,SleepTransition

IP=socket.gethostbyname('yeelink-light-colorb_miap19BE.home') # change to name of device check using arp -a

bulb=Bulb(IP)

inst=sys.argv[1]

match (inst):
  case ("on") : 
    bulb.turn_on()
  case ("off") :
    bulb.turn_off()
  case ("red"):
    bulb.set_rgb(255,0,0)
  case ("white"):
    BulbType(0)
    bulb.set_hsv(0,0,255)
    bulb.set_color_temp(6500)
  case ("yellow"):
    bulb.set_rgb(255,255,200)
    bulb.set_color_temp(3000)
  case ("rgb"):
    r=int(sys.argv[2])
    g=int(sys.argv[3])
    b=int(sys.argv[4])
    bulb.set_rgb(r,g,b)
  case("bright"):
    bright=int(sys.argv[2])
    bulb.set_brightness(bright)
  case ("temp"):
    print(bulb.set_color_temp(int(sys.argv[2])))
  case ("christmas"):
    bulb.start_flow(Flow(3,Flow.actions.recover,yeelight.transitions.christmas(duration=125,sleep=1000)))
  case ("disco"):
    bulb.start_flow(Flow(3,Flow.actions.recover,yeelight.transitions.disco(bpm=120)))
  