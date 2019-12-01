import socket
import sys
import json


jsonResult = {"first":"You're", "second":"Awsome!"}
jsonResult = json.dumps(jsonResult)
try:
    sock = socket.socket()
except socket.error as err:
    print 'Socket error because of %s' %(err)

port = 1500
address = "localhost"

try:
    sock.connect((address, port))
    sock.send(jsonResult)
except socket.gaierror:

    print 'There an error resolving the host'

    sys.exit() 
        
print jsonResult, 'was sent!'
sock.close()