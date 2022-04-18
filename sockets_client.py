# -*- coding: utf-8 -*-
import socket

#Porta do servidor
port = 8084

#Endereço do servidor
dest = 'localhost'

#Mensagem que o cliente envia
msg = 'Olá servidor.'

#Objeto socker
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Conecta ao servidor
print(f'== Conectando a {dest}:{port}==')
client.connect((dest, port))

#Envia mensagem ao servidor
print('== Enviando mensagem ==')
client.send(msg.encode())

#Recebe mensagem do servidor
print('==Recebendo mensagem do servidor ==')
from_server = client.recv(4096)
print(from_server.decode())

#Fecha a conexão
client.close()


