#!/usr/bin/env python3
import os
from _thread import *
import socket

clientes = []

HOST = '127.0.0.1'
PORT = 65432
threadAmount = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((HOST, PORT))
except socket.error as e:
    print(str(e))

print('Aguardando participantes do chat...')
s.listen(5)

print(f'Executando em {HOST}:{PORT}')


def threaded_cli(connection):
    connection.send(str.encode('Bem vindo ao chat'))
    while True:
        data = connection.recv(2048)
        broadcast(data, connection)
    connection.close()


def broadcast(message, connection):
    for _cliente in clientes:
        try:
            _cliente.send(message)
        except:
            _cliente.close


while True:
    Client, addr = s.accept()
    clientes.append(Client)
    print('Conectado a: ' + addr[0] + ':' + str(addr[1]))
    start_new_thread(threaded_cli, (Client, ))
    threadAmount += 1
    print('Usuarios conectados: ' + str(threadAmount))

s.close()
