# -*- coding: utf-8 -*-
import socket
import pickle

class Teste:
    def __init__(self, data):
        self.data = data
    def __str__(self): return self.data

#Porta do servidor
port = 8084

#Endereço do servidor
dest = '192.168.246.20'

#Objeto socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Conecta ao servidor
print(f'== Conectando a {dest}:{port}==')
client.connect((dest, port))

#Envia mensagem ao servidor
n=input('qual a data? ')
print('== Enviando mensagem ==')
data_object = Teste(n)
print(data_object)
data_send = pickle.dumps(str(data_object))
client.send(data_send)

#Recebe mensagem do servidor
print('==Recebendo mensagem do servidor ==')
from_server = client.recv(4096)
z=pickle.loads(from_server)
print(z)


#Fecha a conexão
client.close()


