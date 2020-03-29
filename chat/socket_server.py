# Imports
import socket 
import select 
import sys 
from thread import *
  
# init connection variables and establish connection
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
  
IP_address = '127.0.0.1'
Port = int(5005) 
server.bind((IP_address, Port)) 
  
server.listen(100) 
list_of_clients = [] 
  
# Thread for new Clients  
def clientthread(conn, addr, username): 
    conn.send("Connected to chatroom!") 
    while True: 
            try: 
                message = conn.recv(2048) 
                if message: 
                    print "<" + username + "> " + message 
                    message_to_send = "<" + username + "> " + message 
                    broadcast(message_to_send, conn) 
                else: 
                    remove(conn) 
  
            except: 
                continue

# Send Messages
def broadcast(message, connection): 
    for clients in list_of_clients: 
        if clients!=connection: 
            try: 
                clients.send(message) 
            except: 
                clients.close() 
                remove(clients) 
  
# Remove clients who have disconnected 
def remove(connection): 
    if connection in list_of_clients: 
        list_of_clients.remove(connection) 
  
# Main loop for the chat room   
while True: 
    conn, addr = server.accept() 
    username = conn.recv(2048)
    list_of_clients.append(conn) 
    print username + " has joined the chatroom!"
    start_new_thread(clientthread,(conn,addr, username))     
  
# Exit conditions  
conn.close() 
server.close() 