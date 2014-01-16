"This is a FTP_Server program to send files"

import socket
import threading

class FTP_Server:
	"FTP Server class"
	def __init__(self, sock=None):
		if sock == None:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		else:
			self.sock = sock

	def connect(self, HOST, PORT):
		self.sock.bind((HOST, PORT))
		self.sock.listen(5)
		while 1:
			conn_socket, addr = self.sock.accept()
			print 'Connected to: ', addr
			ct = threading.Thread(target=self.client_thread, args = (conn_socket,))
			ct.run()
		self.sock.close()

	#allows multiple clients to connect and send data
	def client_thread(self, conn_socket):
		while 1:
			data = conn_socket.recv(1024)
			if not data: break
			conn_socket.send(data)
		conn_socket.close()

server = FTP_Server()
conn_socket = server.connect('127.0.0.1', 50007)
