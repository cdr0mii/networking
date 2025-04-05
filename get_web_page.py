import socket

#HOST = 'cdr0mii.github.io'  # The server's hostname or IP address
#HOST = 'google.com'  # The server's hostname or IP address
#HOST = "https:/www.google.com/search?q=food" #use query in url for search
#HOST = "google.com"
#HOST = "i.natgeofe.com"

#E.g.: POTENTIAL RESTAURANT WEBSITE

HOST = "httpbin.org"
PORT = 80       # The port used by the server
#HOST = "https://lh5.googleusercontent.com/p/AF1QipP7lt_fHaJo0ODmy7wq55iOjqtUPPMFIzSKaOXM=w184-h184-n-k-no" #image link
#HOST = "lh5.googleusercontent.com" #image link

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'GET /image/png HTTP/1.0\r\n\r\n')
    #s.sendall(b'GET /images/branding/googleg/1x/googleg_standard_color_128dp.png HTTP/1.1\r\n\r\n')
    #s.sendall(b'GET /p/AF1QipP7lt_fHaJo0ODmy7wq55iOjqtUPPMFIzSKaOXM=w184-h184-n-k-no HTTP/1.1\r\n\r\n')
    #s.sendall(b'GET /search?q=food HTTP/1.1\r\n\r\n') #format the search query
    #s.sendall(b'GET /index.html HTTP/1.1\r\n\r\n')
    for x in range(3):
        data = s.recv(4098)#header info
        #print(data)
        #if(b'Hilltop' in data):
        print('Received', repr(data))
        #print(data)
        #data2 = s.recv(4098)#message body

#import pdb;pdb.set_trace()
#print('Received', repr(data))
