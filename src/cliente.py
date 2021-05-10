#!/usr/bin/env python3
import os
from _thread import *
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print('Cliente conectado')
conexao = True


def thread_read(connection):
    while True:
        data = connection.recv(2048)
        if not data:
            break
        print(b'\nMensagem recebida: '+data)

# def thread_write(connection):


while conexao:
    start_new_thread(thread_read, (s, ))
    value = input('\n\nDigite a mensagem para servidor:\n')
    s.sendall(value.encode())
    print('\n\nMensagem enviada\n')

s.close()
