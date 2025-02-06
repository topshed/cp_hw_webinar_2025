from picozero import LED, Button, Speaker
from time import sleep

l1 = LED(22) # one LED connected to GPIO pin 22
l2 = LED(16) # one LED connected to GPIO pin 16
l3 = LED(13) # one LED connected to GPIO pin 13
l4 = LED(28) # one LED connected to GPIO pin 28
l5 = LED(4)  # one LED connected to GPIO pin 4
leds = [ l1, l2, l3, l4, l5] # list of all the LEDs
b = Button(15) # one button connected to GPIO pin 15
s = Speaker(11) # piezo speaker connected to pin11

running = True # variable to store whether the game is running
speed = 0.5
start = False

def flash(): # function to turn all LEDs on, then off
    for i in range(len(leds)):
        leds[i].on()
    s.play(600,duration=0.5)
    #sleep(0.5)
    for i in range(len(leds)):
        leds[i].off()
    
def loser(): # function to turn all LEDs on, then off one at a time
    for i in range(len(leds)):
        leds[i].on()
    sleep(0.1)
    
    for i in range(len(leds)):
        leds[i].off()
        #sleep(0.3)
    s.play(300,duration=0.4)
    s.play(200,duration=0.5)

def press(): # function to be run when the button is pressed
    print("press")
    s.off()
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
        if l2.is_active:
            
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
                s.play(500,duration=speed/2, wait=False)
                leds[i-1].off()
                sleep(speed)
