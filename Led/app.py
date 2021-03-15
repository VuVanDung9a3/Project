from flask import Flask , render_template, request
import RPi.GPIO as GPIO

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_1 = 17
led_2 = 27
led_3 = 23

led_1Sts = 0
led_2Sts = 0
led_3Sts = 0

GPIO.setup(led_1, GPIO.OUT)
GPIO.setup(led_2, GPIO.OUT)
GPIO.setup(led_3, GPIO.OUT)

GPIO.output(led_1, GPIO.LOW)
GPIO.output(led_2, GPIO.LOW)
GPIO.output(led_3, GPIO.LOW)

@app.route('/')
def hello():
	led_1Sts = GPIO.input(led_1)
	led_2Sts = GPIO.input(led_2)
	led_3Sts = GPIO.input(led_3)
	templateData = {
		'title' : 'RPi Controller WEB',
		'led_1' : led_1Sts,
		'led_2' : led_2Sts,
		'led_3' : led_3Sts
	}
	return render_template("index.html", **templateData)

@app.route('/<deviceName>/<action>')
def action(deviceName, action):
	if deviceName == "led_1":
		actuator = led_1
	if deviceName == "led_2":
		actuator = led_2
	if deviceName == "led_3":
		actuator = led_3
	if action == "on":
		GPIO.output(actuator, GPIO.HIGH)
	if action == "off":
		GPIO.output(actuator, GPIO.LOW)

	led_1Sts = GPIO.input(led_1)
	led_2Sts = GPIO.input(led_2)
	led_3Sts = GPIO.input(led_3)

	templateData = {
		'led_1' : led_1Sts,
		'led_2' : led_2Sts,
		'led_3' : led_3Sts
	}
	return render_template("index.html", **templateData)

if __name__ == "__main__":
	app.run(host = '0.0.0.0', debug=True)
