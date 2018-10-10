import gc
import sys
from math import trunc
from urequests import get
import ujson
from utime import sleep
from utime import sleep_ms
from machine import Pin, reset
from neopixel import NeoPixel
from umqtt.robust import MQTTClient


# Define some basic colours
led_off = (0, 0, 0)
led_red = (32, 0, 0)
led_green = (0, 32, 0)
led_blue = (0, 0, 32)

with open("./config.json") as fp:
    config = ujson.load(fp)

pin = Pin(config["neopixel_pin"], Pin.OUT) 
np = NeoPixel(pin, 24)

heartbeat = Pin(2, Pin.OUT)  # Pin 2 is connected to the blue LED on Wemos board

client = MQTTClient(config["mqtt_client"], config["mqtt_server"])

############## Here we go then #################

def goGauge():
    spin_the_ring()  # just for fun we will spin the pixels on the ring to show we're starting

    client.set_callback(do_callback)

    if not client.connect(clean_session=False):
        print("New session being set up")
        client.subscribe(config["mqtt_topic"])

    while 1:
        client.check_msg()  # non-blocking check for new data
        heartbeat.off()  # let people know we are still working
        sleep(1)
        heartbeat.on()
        sleep(config["poll_interval"])
        gc.collect()


def do_callback(topic, msg):
    value = str(msg, "utf-8")
    print("value: " + value)
    val = float(value)
    print(val)
    neopixel_display(val)


def spin_the_ring():
    # If we are running on micropython then spin the LED's on the ring
    np.fill(led_off)
    np.write()
    for i in range(0, 24):
        np[i] = led_blue
        if i > 0:
            np[i - 1] = led_green
        if i > 1:
            np[i - 2] = led_red
        if i > 2:
            np[i - 3] = led_off
        np.write()
        sleep_ms(50)
    np.fill(led_off)
    np.write()


def neopixel_display(value):
    np.fill(led_off)
    np.write()
    
    if value < config["max"]["max_value"]:
        for i in range(0,config["pixel_count"]):
            if value >= config["pixels"][i]["min_val"]:
                np[i] = (config["colours"][config["pixels"][i]["colour"]][0],
                         config["colours"][config["pixels"][i]["colour"]][1],
                         config["colours"][config["pixels"][i]["colour"]][2])
    else:
        for n in range(0,24):
            np[n] = (config["colours"][config["max"]["colour"]][0],
                     config["colours"][config["max"]["colour"]][1],
                     config["colours"][config["max"]["colour"]][2])
        
    np.write()



# If we are being imported as a module then do nothing
# If we are being run as a script then run
if __name__ == '__main__':
    gc.enable()
    try:
        goGauge()
    except:
        print("something has gone wrong")
        sleep(60)
        reset()
