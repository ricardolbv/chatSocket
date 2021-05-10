#!/usr/bin/env python3
import os
from _thread import *
import socket

clientes = {}

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
    ##nome = connection.recv(2048)
    ##msgInicial = 'Bem vindo ao chat ' + nome.decode()
    # connection.send(str.encode(msgInicial))
    while True:
        data = connection.recv(2048)
        broadcast(data, connection)
    connection.close()


def broadcast(message, connection):
    for nome, _cliente in clientes:
        try:
            _cliente.send(message)
        except:
            _cliente.close


def dealingWithCli(client, nome):
    clientes[nome]: client


while True:
    Client, addr = s.accept()
    # clientes.append(Client)
    nome = Client.recv(2048)
    msgInicial = 'Bem vindo ao chat ' + nome.decode()
    Client.send(str.encode(msgInicial))
    dealingWithCli(Client, nome)
    print('Conectado a: ' + addr[0] + ':' + str(addr[1]))

    start_new_thread(threaded_cli, (Client, ))
    threadAmount += 1
    print('Usuarios conectados: ' + str(threadAmount))

s.close()
