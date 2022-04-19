# -*- coding: utf-8 -*-
#Biblioteca sockets
import socket
import pickle


class NoticiaResp:
    noticias = {
        '2022_04_19': [
            'Arma abandonada em árvore após ataque em Guarapuava é uma espingarda e foi roubada de empresa de valores, diz polícia',
            'Furtos de celular pela janela de carros de aplicativo viram rotina e assustam passageiros cariocas'
        ],
        '2022_04_18': [
            'Vice da Câmara diz que Mourão tenta normalizar a tortura: ‘Não parece ter vergonha na cara’...',
            'Armas e cachaça: como jovens ianomâmi são recrutados para trabalho no garimpo ilegal'
        ]
    }

    def __init__(self, data):
        self.data = data
    
    def get_data(self):
        return self.data

    def get_noticia(self):
        return NoticiaResp.noticias[self.get_data()]


#Porta do servidor
port = 8084

#Objeto socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Associa o socket a uma porta local
serv.bind(('0.0.0.0', port))
serv.listen()

#Servidor fica aguardando conexões
while True:
    print(f'*** Servidor aguardando conexões na porta {port} ***')
    conn, addr = serv.accept()
    print(f'== Conexao recebida de {addr} ==')
 
    #Recebe os dados
    dados = conn.recv(4096)
    
    data_object = pickle.loads(dados)
    print('== Dados recebidos: ==')
    print(data_object)

    # cria objeto de resposta
    response_object = NoticiaResp(data_object)

    # responde
    conn.send(pickle.dumps(response_object.get_noticia()))

    #Fecha a conexao
    conn.close() 
    print('== Cliente desconectado ==')
