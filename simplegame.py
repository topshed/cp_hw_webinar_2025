from picozero import LED, Button
from time import sleep

l1 = LED(22) # one red LED connected to GPIO pin 22
l2 = LED(16) # one green LED connected to GPIO pin 16
l3 = LED(13) # one red LED connected to GPIO pin 13
l4 = LED(28) # one red LED connected to GPIO pin 28
l5 = LED(4)  # one red LED connected to GPIO pin 4
leds = [ l1, l2, l3, l4, l5] # list of all the LEDs
b = Button(15) # one button connected to GPIO pin 15

running = True # variable to store whether the game is running
speed = 0.5 # the time between LEDs turning on/off

def press(): # function to be run when the button is pressed
    global running
    global speed
    running = not running # toggle the running variable
    speed = speed*0.95 # set the speed to 95% of its previous value
    if l2.is_active:    # if the green LED is on...   
        running = True # carry on playing
    else:
        speed = 0.5 # set the speed back to the starting value
                   
b.when_pressed = press # set the function to be run when pressed

while True:
    # loop through values of i from 0 to the length of the LEDs list
    for i in range(len(leds)):
        if running == True:
            leds[i].on()  # turn the ith LED on
            leds[i-1].off() # turn the previous LED off
            sleep(speed)
