#Biblioteca sockets
import socket
from threading import Thread
import time

#Porta do servidor
port = 8084

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

        #Trata os dados recebidos
        from_client = data
        print(from_client.decode())

        #Envia uma mensagem
        self.conn.send(msg.encode())
        
        # time.sleep(5) #Aguarda antes de fechar a conexão

        #Fecha a conexao
        self.conn.close()
        print('client disconnected')


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
    ThreadServer(addr,conn).start()
    print("Fim da iteração\n")
