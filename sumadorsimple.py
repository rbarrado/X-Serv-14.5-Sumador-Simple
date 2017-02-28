#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Simple HTTP Server
Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket
import random

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

#creamos el socket
#Se lee así: del modulo socket utiliza el metodo socket (socket.socket)
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1234))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)

sumador = 0;
try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        peticion = recvSocket.recv(2048).decode("utf-8", "strict")
        try:
            sumando1 = peticion.split()[1][1:]
            print (sumando1)
            if sumando1 == "favicon.ico":
                continue
            print('Answering back...')
            if (sumador == 0):            
                sumador = sumando1         
                resultado = "Me has enviado un " + str(sumador) + " .Dame otro mas"
            else:             
                sumando2 = sumando1
                resultado = int(sumador) + int(sumando2)
                resultado = "Me habias enviado un " + str(sumador) + " . Ahora un " + str(sumando2) + ". La suma es: " + str(resultado)
                sumador = 0
            recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                            "<html><body><h1>" + resultado + "</h1></body></html>" +
                            "\r\n", 'utf-8'))
            recvSocket.close()
        except ValueError:
            recvSocket.close()
except KeyboardInterrupt:
    mySocket.close()
