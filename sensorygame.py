from picozero import LED, Button, PWMLED
from time import sleep

l1 = LED(16)
l2 = LED(17)
l3 = LED(18)
l4 = LED(19)
l5 = PWMLED(20) # This is a PWM LED so we can make it pulse
leds = [ l2, l3, l4, l1, l5] # list of all the LEDs
b = Button(21)

running = True # variable to store whether the game is running
speed = 0.5
start = False

def flash(): # function to turn all LEDs on, then off
    for i in range(len(leds)):
        leds[i].on()
    sleep(0.5)
    for i in range(len(leds)):
        leds[i].off()
    
def loser(): # function to turn all LEDs on, then off one at a time
    for i in range(len(leds)):
        leds[i].on()
    sleep(0.1)
    for i in range(len(leds)):
        leds[i].off()
        sleep(0.3)

def press(): # function to be run when the button is pressed
    print("press")
    global running
    global speed
    global start
    if not start:
        start = True
        running = True
    else:
        running = not running
        speed = speed*0.95
        print(speed)
        if l5.is_active:
            flash()
            running = True
        else:
            start = False
            speed = 0.5
            loser()
            l5.pulse()
                   
b.when_pressed = press

l5.pulse() # pulse the LED

while True:
    if start:
        for i in range(len(leds)):
            if running == True:
                leds[i].on()
                if i != 0:
                    leds[i-1].off()
                elif i == 0:
                    leds[-1].off()
                sleep(speed)
