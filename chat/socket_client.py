# Imports
import socket 
import select 
import sys 

# Make sure user has provided an username
if len(sys.argv) != 2: 
    print "Please enter your username"
    exit() 

# init connection variables and establish connection
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
IP_address = '127.0.0.1'
Port = int(5005) 

Username = str(sys.argv[1])
server.connect((IP_address, Port)) 
server.send(Username)

# main loop for chat room
open = True
while open: 
    sockets_list = [sys.stdin, server] 
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[]) 
  
    for socks in read_sockets: 
        if socks == server: 
            message = socks.recv(2048) 
            print message 
        else: 
            message = sys.stdin.readline() 
            if message.rstrip("\n") == "Quit" :
                message = Username +" has left the chat room"
                server.send(message) 
                open = False
            else: 
                server.send(message) 
                sys.stdout.write("<You>") 
                sys.stdout.write(message) 
                sys.stdout.flush() 
server.close() 