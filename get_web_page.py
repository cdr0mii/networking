import socket

HOST = 'cdr0mii.github.io'  # The server's hostname or IP address
#HOST = 'google.com'  # The server's hostname or IP address
PORT = 8080        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'GET /index.html HTTP/1.1\r\n\r\n')
    #s.sendall(b'GET /index.html HTTP/1.1\r\n\r\n')
    data = s.recv(2048)#header info
    data2 = s.recv(2048)#message body

#import pdb;pdb.set_trace()
print('Received', repr(data2))