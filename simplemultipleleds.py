from picozero import LED
from time import sleep

l1 = LED(22) # one LED connected to GPIO pin 22
l2 = LED(16) # one LED connected to GPIO pin 16
l3 = LED(13) # one LED connected to GPIO pin 13
l4 = LED(28) # one LED connected to GPIO pin 28
l5 = LED(4)  # one LED connected to GPIO pin 4

leds = [l1,l2,l3,l4,l5] # A list of all the LEDs


while True:
    # loop through values of i from 0 to the length of the LEDs list
    for i in range(len(leds)):  
        leds[i].on() # turn the ith LED on
        leds[i-1].off() # turn the previous LED off
        sleep(0.3)