import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket criado com sucesso . . . . .")
host = 'localhost'
porta = 5433

connection.bind((host, porta))
msg = 'Hello Cliente'

while 1:
    dados, endereco = connection.recvfrom(4096)

    if dados:
        print("Servidor enviando mensagem . . . . .")
        connection.sendto(dados + (msg.encode()), endereco)