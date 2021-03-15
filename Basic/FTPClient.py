import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

port = 5050
host = socket.gethostname()

s.connect((host, port))
s.send(b"Hello server")

with open('received.txt', 'wb') as f:
	print('file opend')
	while True:
		print('receiving data')
		data = s.recv(1024)
		print('data = %s',(data))
		if not data:
			break
		f.write(data)
f.close()
print('Succesfully get the file')
s.close()
print('connection closed')