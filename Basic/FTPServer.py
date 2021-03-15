import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
port = 5050
host = socket.gethostname()
s.bind((host, port))
s.listen(5)
print("Server listening")

while True:
	conn, addr = s.accept()
	print("Got connection from", addr)
	data = conn.recv(1024)
	print("Server received", repr(data))

	filename = 'mytext.txt'
	f = open(filename, 'rb')
	in_data = f.read(1024)
	while(in_data):
		conn.send(in_data)
		print('Sent ',repr(in_data))
		in_data = f.read(1024)
	f.close()

	print('Done sending')
	conn.send(b'Thank you for connecting')
	conn.close()
