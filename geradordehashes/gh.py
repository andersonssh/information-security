import hashlib
string = input('Digite um texto para gerar um hash: ')

menu = int(input('''#### MENU - ESCOLHA O TIPO DE HASH ###
                1) MD5
                2) SHA1
                3) SHA256
                4) SHA512
                Digite o número do hash a ser gerado: '''))

#utf-8 para aceitar acentuacoes e ç
if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
else:
    print('Número inválido')

print(f'O hash da string {string} é: {resultado.hexdigest()}')
