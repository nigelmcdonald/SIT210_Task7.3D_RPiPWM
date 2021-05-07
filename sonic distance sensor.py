import RPi.GPIO as GPIO
import time
from gpiozero import DistanceSensor

#variables
pisoPin = 21
blueLED = 25
yellowLED = 12
redLED = 24
soundVCC = 25
Hz = 0
distance = 100

# pin setup
GPIO.setmode(GPIO.BCM)# use BCM to get GPIO pin mode not pin number mode for pins
sensor = DistanceSensor(trigger = 18, echo = 16)
GPIO.setwarnings(False)
GPIO.setup(blueLED, GPIO.OUT)
GPIO.setup(yellowLED, GPIO.OUT)
GPIO.setup(redLED, GPIO.OUT)
GPIO.setup(pisoPin, GPIO.OUT)
GPIO.setwarnings(False)

#create a PWM instance
p = GPIO.PWM(pisoPin, 100)  # channel=pisoPin frequency=100Hz
p.start(0)#  star PWM instance where the value is the duty cycle (0.0 <= value <= 100.0)
try:   
    while True:
        #print(distance) # uncomment to see printout of distance
        if distance <= 10: # set a specific LED based on distance from the sensor
            GPIO.output(redLED, GPIO.HIGH)
            GPIO.output(yellowLED, GPIO.LOW)
            GPIO.output(blueLED, GPIO.LOW)
        elif (distance > 10) and (distance <= 20):
            GPIO.output(redLED, GPIO.LOW)
            GPIO.output(yellowLED, GPIO.HIGH)
            GPIO.output(blueLED, GPIO.LOW)
        elif distance > 20:
            GPIO.output(redLED, GPIO.LOW)
            GPIO.output(yellowLED, GPIO.LOW)
            GPIO.output(blueLED, GPIO.HIGH)        
        p.ChangeDutyCycle(100/distance) # set dutycycle for the pezo buzzer to change its pitch
        time.sleep(0.2) # read data every this many seconds
        distance = sensor.distance # read data
        distance = round(distance, 2) # round to 2 decimals
        distance = distance * 100 # convert to cm
except KeyboardInterrupt: # break loop with cntrl c
    pass
p.stop()
GPIO.cleanup()

