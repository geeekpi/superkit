from machine import Pin
import utime as time
from dht import DHT11


DHTPin = Pin(15, Pin.OUT, Pin.PULL_DOWN)

while True:
    time.sleep(1)
    sensor = DHT11(DHTPin)
    sensor.measure()
    t = (sensor.temperature())
    h = (sensor.humidity())
    
    print("Temperature: " + str(t))
    print("Humidity: " + str(h))
    
    
