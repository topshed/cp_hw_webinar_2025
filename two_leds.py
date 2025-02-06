from picozero import LED

l1 = LED(22) # one LED connected to GPIO pin 22
l2 = LED(16) # one LED connected to GPIO pin 16

l1.blink() # start blinking the LED on and off
l2.blink() # start blinking the LED on and off
