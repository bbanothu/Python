# Imports
import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)

# main loop for chat room
open = True
while open: 
        MESSAGE = sys.stdin.readline() 
        if MESSAGE.rstrip("\n") == "Quit" :
            print >>sys.stderr, 'Quitting server'
            MESSAGE = "Client has terminated the connection"
            sent = sock.sendto(MESSAGE, server_address)
            break
        else:
            # Send data
            print >>sys.stderr, 'sending "%s"' % MESSAGE
            sent = sock.sendto(MESSAGE, server_address)
            # Receive response
            print >>sys.stderr, 'waiting to receive'
            data, server = sock.recvfrom(4096)
            print >>sys.stderr, 'received "%s"' % data


print >>sys.stderr, 'closing socket'
sock.close()