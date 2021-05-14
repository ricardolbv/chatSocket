#!/usr/bin/env python3
import os
from _thread import *
import socket
import json
from typing import ContextManager

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print('Cliente conectado')
conexao = True

# Tipo de mensagem que será trocada no servidor
# Type pode ser: Mensagem, Cadastro, Descadastro
mensagem = {'sender': '', 'type': '', 'content': ''}


def comunication(sender, type, content, connection):
    mensagem['sender'] = sender
    mensagem['type'] = type
    mensagem['content'] = content
    msg = json.dumps(mensagem)
    connection.sendall(msg.encode())


def thread_read(connection):
    while True:
        data = connection.recv(2048)
        # if not data:
        #    break
        msg = data.decode()
        _msg = json.loads(msg)
        print(_msg['sender']+' diz : '+_msg['content'])


# Enviando o nome do cliente ao servidor
while True:
    name = input('\n\nDigite seu username:\n')
    s.sendall(name.encode())
    data = s.recv(2048)
    msg = data.decode()
    _msg = json.loads(msg)
    if(_msg['type'] != 'error'):
        print(_msg['content'])
        break
    print(_msg['content'])

while conexao:
    start_new_thread(thread_read, (s, ))
    value = input('>>')
    # s.sendall(value.encode())
    comunication(name, 1, value, s)

s.close()
