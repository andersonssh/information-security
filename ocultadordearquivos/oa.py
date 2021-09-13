import ctypes

#funciona
#linha equivalente a ir em propriedades e marcar a opcao "ocultar arquivo"
#atributo ocultar tem o hexadecimal equivalente a afirmação acima
atributo_ocultar = 0x02

pasta = input('Digite o caminho da pasta a ser ocultada ex (C:/pasta): ')
retorno = ctypes.windll.kernel32.setFileAttributesW(pasta, atributo_ocultar)

if retorno:
    print('O arquivo foi  ocultado')

else:
    print('O arquivo não foi ocultado')