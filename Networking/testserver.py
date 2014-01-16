import sys, syslog, socket, string, os

class config:
	welcome_message = "this is just too late"
	max_cmd_then = 255
	storage_path = "/Users/anuj/devel/ftp"
	debug = 1 #verbose debugging
	filename_goochars = string.letters + string.digits + ".-_"

class peer:
	sock = socket.fromfd(sys.stderr.fileno(), socket.AF_INET, socket.SOCK_STREAM)
	ip = sock.getpeername()[0]
	dataport = None

def reply(x):
	sys.stderr.write(x + "\r\n")
	if config.debug:
		syslog.syslog("R: "+repr(x))

def create_datasock():
	if not peer.dataport:	
