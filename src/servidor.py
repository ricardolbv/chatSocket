#!/usr/bin/env python3
import os
from _thread import *
import socket
import json

clientes = {}

HOST = '127.0.0.1'
PORT = 65432
threadAmount = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


mensagem = {'sender': '', 'type': '', 'content': ''}


def comunication(sender, type, content, connection):
    mensagem['sender'] = sender
    mensagem['type'] = type
    mensagem['content'] = content
    msg = json.dumps(mensagem)
    connection.sendall(msg.encode())


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
        msg = data.decode()
        _msg = json.loads(msg)
        print(_msg)
        if(_msg['content'] == 'sair'):
            print(_msg['sender']+' Quer sair')
            removeCli(_msg['sender'], connection)
        else:
            broadcast(data, connection)


def broadcast(message, connection):
    for key in clientes:
        try:
            if(clientes[key] != connection):
                clientes[key].send(message)
        except:
            clientes[key].close()


def verifyUser(user):
    for key in clientes:
        if(key == user):
            return False  # Username já cadastrado
    return True  # Username validado


def removeCli(client, connection):
    connection.close()
    clientes.pop(client, None)
    sendOnlineClients()


# Envia lista de clientes online para todos os cadastrados
def sendOnlineClients():
    clientesOnline = str(clientes.keys())
    _msg = 'Usuarios online'+str(clientesOnline[9:])
    for key in clientes:
        try:
            comunication('server', 'info', _msg, clientes[key])
        except:
            clientes[key].close()


while True:
    Client, addr = s.accept()
    while True:  # Loop de validação de username informado por clientes
        nome = Client.recv(2048)
        nome = nome.decode()
        if verifyUser(nome):
            clientes.update({str(nome): Client})
            sendOnlineClients()
            break
        comunication('server', 'error', 'Nome já esta sendo utilizado', Client)

    print('Conectado a: ' + addr[0] + ':' + str(addr[1]))
    start_new_thread(threaded_cli, (Client, ))
    threadAmount += 1
    print('Usuarios conectados: ' + str(threadAmount))


s.close()
