import socket


s = socket.socket()

print "Socket created ..."


port = 1516

s.bind(('', port))

s.listen(5)

print 'socket is listening'


while True:
    c, addr = s.accept()
    print 'got connection from ', addr

    c.send('Thank you for connect to me!')

    c.close()
