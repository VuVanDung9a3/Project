import socket

request = b"""\
GET /download/ HTTP/1.0
Host: www.python.org"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

s.connect(("www.python.org", 80))
s.sendall(request)
data = s.recv(8192)
print(data)