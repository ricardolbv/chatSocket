#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
#s.sendall(b'He, world')
#data = s.recv(1024)
#print('Received', repr(data))
print('Cliente conectado')
conexao = True

while conexao:
    data = s.recv(1024)
    print(f'ssss:{data}')
    value = input('\n\nDigite a mensagem para servidor:\n')
    s.sendall(value.encode())
    print('\n\nMensagem enviada\n')

s.close()
