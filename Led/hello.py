import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 25

GPIO.setup(led, GPIO.OUT)
GPIO.output(led, GPIO.LOW)
while True:
	GPIO.output(led, GPIO.HIGH)
	print("the led turn on")
	time.sleep(1)
	GPIO.output(led,GPIO.LOW)
	print("the led turn off")
	time.sleep(1)
