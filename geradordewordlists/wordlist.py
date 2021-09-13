import itertools

#(entrada de string, numero da saida da permutacao)
# resultado = itertools.permutations('abc', 2)
# for i in resultado:
#     #junta os elementos da tupla
#     print(''.join(i))
#
# print('FIM 1\n')

string = input('Palavra a permutar: ')
resultado = itertools.permutations(string, len(string))

for i in resultado:
    print(''.join(i))