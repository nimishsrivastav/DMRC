# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12345

# connect to the server on local computer
s.connect(('192.168.100.2', port))

# receive d
# ata from the server

var= s.recv(1024)

output='Hi'
s.sendall(output.encode('utf-8'))

print( var.decode('utf-8'))
# close the connection
s.close()