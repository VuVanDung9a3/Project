import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

motor1 = 14
motor2 = 15
motor3 = 4
motor4 = 17

GPIO.setup(motor1, GPIO.OUT)
GPIO.setup(motor2, GPIO.OUT)
GPIO.setup(motor3, GPIO.OUT)
GPIO.setup(motor4, GPIO.OUT)

def backward():
	GPIO.output(motor1, GPIO.HIGH)
	GPIO.output(motor2, GPIO.LOW)
	GPIO.output(motor3, GPIO.HIGH)
	GPIO.output(motor4, GPIO.LOW)
def forward():
        GPIO.output(motor1, GPIO.LOW)
        GPIO.output(motor2, GPIO.HIGH)
        GPIO.output(motor3, GPIO.LOW)
        GPIO.output(motor4, GPIO.HIGH)
def turnLeft():
        GPIO.output(motor1, GPIO.HIGH)
        GPIO.output(motor2, GPIO.LOW)
        GPIO.output(motor3, GPIO.LOW)
        GPIO.output(motor4, GPIO.HIGH)
def turnRight():
        GPIO.output(motor1, GPIO.LOW)
        GPIO.output(motor2, GPIO.HIGH)
        GPIO.output(motor3, GPIO.HIGH)
        GPIO.output(motor4, GPIO.LOW)
def stop():
        GPIO.output(motor1, GPIO.LOW)
        GPIO.output(motor2, GPIO.LOW)
        GPIO.output(motor3, GPIO.LOW)
        GPIO.output(motor4, GPIO.LOW)

