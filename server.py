import socket
from _thread import *
import json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

with open('config.json') as f:
    config = json.load(f)

server.bind((config['host'], config['port']))
server.listen(100)

clients = []

def clientthread(conn, addr):
    conn.send("MOTD hello world".encode())

    while True:
        try:
            message = conn.recv(2048)

            if message:
                print("<" + addr[0] + "> " + message.decode())
                response = message
                broadcast(message, conn)
            else:
                remove(conn)
        except Exception as e:
            print(f"Error: {e}")
            break

def broadcast(message, connection):
    for client in clients:
        if clients != connection:
            try:
                clients.send(message.encode())
            except:
                remove(clients)

def remove(connection):
    if connection in clients:
        clients.remove(connection)

while True:
    conn, addr = server.accept()
    clients.append(conn)
    print(addr[0] + " connected")
    start_new_thread(clientthread, (conn, addr))

conn.close()
server.close()