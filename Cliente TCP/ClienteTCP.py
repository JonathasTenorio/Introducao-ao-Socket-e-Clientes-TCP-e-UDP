import socket
import sys


def main():
    try:
        # AF_INET = Representa o protocolo IP/ SOCK_STREAM = Representa o protocolo TCP.
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou")
        print("Erro: {}".format(e))
        sys.exit()

    print("Socket criado com sucesso!!")

    HostAlvo = input("Digite o host ou IP a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")

    try:
        connection.connect((HostAlvo, int(PortaAlvo)))
        print("Cliente TCP conectado com sucesso no host: " + HostAlvo + " e na porta: " + PortaAlvo)
        connection.shutdown(2)
    except socket.error as e:
        print("A conexão falhou! Não foi possível se conectar ao host " + HostAlvo + " na porta " + PortaAlvo)
        print("Error: {}".format(e))
        print("Verifique o host ou a porte e tente novamente . . . . .")
        sys.exit()


if __name__ == "__main__":
    main()
