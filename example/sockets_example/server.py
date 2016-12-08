#!/usr/bin/python2.7

import socket

ssocket = socket.socket()

ssocket.bind(("", 8841))
ssocket.listen(1)
connection, adress = ssocket.accept()

while True:
    data = connection.recv(1024)
    if not data:
        break
    connection.send(data.upper())
