import socket
import pickle
from threading import Thread
import time


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


class ThreadServer(Thread):
    def __init__ (self, addr, conn):
        Thread.__init__(self)
        self.addr = addr
        self.conn = conn

    def run(self):
        #Mensagem que o servidor envia
        msg = 'Eu sou o SERVIDOR. Thread atendendo {}'.format(self.addr)
        
        print("Thread servindo cliente ", self.addr)
        
        print('Dados da conexão: ', self.conn)
        
        #Recebe os dados
        data = self.conn.recv(4096)

        # cria objeto de resposta
        response_object = NoticiaResp(pickle.loads(data))

        # responde
        self.conn.send(pickle.dumps(response_object.get_noticia()))
        
        time.sleep(3) #Aguarda antes de fechar a conexão

        #Fecha a conexao
        self.conn.close()
        print('client disconnected')


#Porta do servidor
port = 8084

#Objeto socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Associa o socket a uma porta local
serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Possibilita reusar portas
serv.bind(('0.0.0.0',port))
serv.listen()

#Servidor fica aguardando conexões. 
#Quando receber uma conexão, repassa para um thread processar a conexão
while True:
    print("Aguardando novas conexões...")
    conn, addr = serv.accept()
    print(f'== Conexao recebida de {addr} ==')
    ThreadServer(addr,conn).start()
    print("Fim da iteração\n")