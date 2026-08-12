from machine import Pin
from neopixel import NeoPixel
import time

np = NeoPixel(Pin(7),1)

np.fill((10,10,10)); np.write()

valve = Pin(2, Pin.OUT)

while True:
  
    np.fill((10,0,0));np.write()
    valve.on()
    time.sleep(3)
      
    np.fill((0,10,0));np.write()
    valve.off()
    time.sleep(3)
