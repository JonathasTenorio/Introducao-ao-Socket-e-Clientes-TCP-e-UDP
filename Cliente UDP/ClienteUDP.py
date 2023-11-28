import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Cliente socket criado com sucesso")

host = 'localhost'
porta = 5433

msg = '\nHello server'

try:
    print('Cliente: ' + msg)
    connection.sendto(msg.encode(), (host, 5433))

    dados, servidor = connection.recvfrom(4096)
    dados = dados.decode()
    print("Cliente: " + dados)

finally:
    print("Cliente: Fechando a conexão . . . . .")
    connection.close()