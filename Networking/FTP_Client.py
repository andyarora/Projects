import socket

HOST = '127.0.0.1'
PORT = 50007

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
sock.send('This is test 1')
data = sock.recv(1024)
sock.close()
print 'received', repr(data)
