import socket

#HOST = 'cdr0mii.github.io'  # The server's hostname or IP address
#HOST = 'google.com'  # The server's hostname or IP address
#HOST = "https:/www.google.com/search?q=food" #use query in url for search
HOST = "google.com"
PORT = 80       # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'GET /search?q=food HTTP/1.1\r\n\r\n') #format the search query
    #s.sendall(b'GET /index.html HTTP/1.1\r\n\r\n')
    for x in range(20):
        data = s.recv(4098)#header info
        #print(data)
        #if(b'Hilltop' in data):
        print('Received', repr(data))
        #print(data)
        #data2 = s.recv(4098)#message body

#import pdb;pdb.set_trace()
#print('Received', repr(data))