import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Cliente Socket criado!')

host = 'localhost'
porta = 5433
mensagem = 'Ola, servidor'

try:
    print('Cliente: ' + mensagem)
    s.sendto(mensagem.encode(), (host, porta))
    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print('Cliente: ' + dados)
    print(servidor)
finally:
    print('Cliente fechando a conexão')
    s.close()
