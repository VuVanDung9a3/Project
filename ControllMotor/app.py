  
from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import motor
motor.stop()

app = Flask(__name__)

@app.route('/')
def hello():
	return render_template("index.html" )

@app.route('/<changePin>', methods = ['POST'])
def change(changePin):
	changePin = int(changePin)
	if changePin == 1:
		motor.turnLeft()
	elif changePin == 2:
		motor.forward()
	elif changePin == 3:
                motor.turnRight()
	elif changePin == 4:
                motor.backward()
	elif changePin == 5:
                motor.stop()
	else:
		print("Wrong command")

	return render_template("index.html")
if __name__ == "__main__":
	app.run(debug=True)
