import RPi.GPIO as GPIO
import time
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(20, GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(16, GPIO.OUT,initial=GPIO.HIGH)

time.sleep(2)
red = GPIO.PWM(21,1000)
red.start(99)
blue = GPIO.PWM(20,1000)
blue.start(99)
green = GPIO.PWM(16,1000)
green.start(99)
time.sleep(2)

#red.ChangeDutyCycle(99)
#blue.ChangeDutyCycle(99)
#green.ChangeDutyCycle(99)
while(1):
  time.sleep(1)
