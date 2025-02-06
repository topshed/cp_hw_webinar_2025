from picozero import LED
from time import sleep

l1 = LED(22) # one LED connected to GPIO pin 16
l2 = LED(16)
l3 = LED(13) # one LED connected to GPIO pin 16
l4 = LED(28)
l5 = LED(4)

leds = [l1,l2,l3,l4,l5]


while True:
    for i in range(len(leds)):
        leds[i].on()
        if i != 0:
            leds[i-1].off()
        elif i == 0:
            leds[-1].off()
        sleep(0.3)
