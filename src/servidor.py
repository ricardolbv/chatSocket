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
    while True:
        data = connection.recv(2048)
        broadcast(data, connection)
    connection.close()


def broadcast(message, connection):
    for key in clientes:
        try:
            if(clientes[key] != connection):
               #remetente = key.decode()
               #_msg = message.decode()
               #_msgCompleta = '<'+remetente+'> :'+message
               # print(_msgCompleta)
                clientes[key].send(message)
        except:
            clientes[key].close()


while True:
    Client, addr = s.accept()
    nome = Client.recv(2048)
    msgInicial = 'Bem vindo ao chat ' + nome.decode()
    Client.send(str.encode(msgInicial))
    clientes.update({nome: Client})
    print('Conectado a: ' + addr[0] + ':' + str(addr[1]))

    start_new_thread(threaded_cli, (Client, ))
    threadAmount += 1
    print('Usuarios conectados: ' + str(threadAmount))
    print(clientes)

s.close()
