

import socket
import sys

try:
    s = socket.socket(socket.AF_INET)
except socket.error as err:
    print 'Socket error because of %s' %(err)

port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:

    print 'There an error resolving the host'

    sys.exit() 
        
s.connect((host_ip,port))
print 'The socket was succesfully connected with google \
on port == %s' %(host_ip)