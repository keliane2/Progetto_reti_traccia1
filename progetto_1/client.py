#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#client 

import socket
from threading import Thread

# IP address del server ricevente
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5001
# riceve 1024 bytes
BUFFER_SIZE = 1024


def receive():
    # gestisce la ricezione di messaggi
    while True:
        try:
            message = client_socket.recv(BUFFER_SIZE).decode('utf-8')
            if message:
                print(message)
        except:
            print("An error occurred!")
            client_socket.close()
            break

def send():
    # gestisce l'invio dei messaggi
    while True:
        message = input('')
        client_socket.send(bytes(message, "utf-8"))

if __name__ == "__main__":
    # Creazione del socket del client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))  # Connessione al server

    # Avvio dei thread per ricevere e inviare messaggi
    receive_thread = Thread(target=receive)
    receive_thread.start()

    send_thread = Thread(target=send)
    send_thread.start()
