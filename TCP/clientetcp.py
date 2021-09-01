import socket
import sys


def main():
    #AF_INET sinaliza protocolo ip
    #SOC_STREAM sinaliza tcp
    #0 sinaliza o protocolo de comunicação com o servidor (TCP)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print(f'A conexão falhou!!\nErro: {e}')
        sys.exit()
    print('Socket criado!')

    hostAlvo = input('Digite o Host ou Ip a ser conectado:')
    portaAlvo = input('Digite a porta a ser conectada: ')

    try:
        s.connect((hostAlvo, int(portaAlvo)))
        print(f'Cliente TCP conectado! {hostAlvo}:{portaAlvo}')
        s.shutdown(2)
    except socket.error as e:
        print(f'A conexão com {hostAlvo}:{portaAlvo}')
        print(f'Erro: {e}')
        sys.exit()

if __name__ == '__main__':
    main()