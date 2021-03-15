#import re
#line = "Hoc Python la de hoc hon Java?"
#matchObj = re.match(r'(.*) la (.*?) .*', line, re.M|re.I)
#if matchObj:
#	print("matchObj.group(): ", matchObj.group())
#	print("matchObj.group(1): ", matchObj.group(2))
#	print("matchObj.group(2): ", matchObj.group(3))
#else:
#	print("Khong ket noi")

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'
@app.route('/user/<username>')
def profile(username):
	return 'Hello %s' %username

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')