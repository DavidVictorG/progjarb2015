import sys
import socket
import io


HOST, PORT = '', 8888
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# Bind the socket to the port
sock.bind((HOST,PORT))
sock.listen(1)
print 'starting up on port %s' % PORT
# sock.bind(server_address)

while True:
    	# Wait for a connection
    	# print >>sys.stderr, 'waiting for a connection'
    	connection, client_address = sock.accept()
    
	filename = data.split()
	file1 =filename[1]	
	file2 =file1[1:]
	print file2
	f= open(file2+".jpg",'r+')
	jpgdata2 = f.read()
	f.close()
	http_response = "\HTTP/1.1 200 OK \n\n%s"%jpgdata2

        # Clean up the connection
	connection.sendall(http_response)
	connection.close()
