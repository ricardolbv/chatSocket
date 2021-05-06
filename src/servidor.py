#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 65432
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print(f'Runnint at {HOST}:{PORT}')
conn, addr = s.accept()
conexao = True

while conexao:
    print('Connected by', addr)
    data = conn.recv(1024)
    print(f'ccccc: {data}\n\n')
    if data is 'fechar':
        break
    value = input('Digite mensagem para cliente:\n')
    conn.sendall(value.encode())
    print('Mensagem enviada')

s.close()
