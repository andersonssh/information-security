import hashlib

arq1 = 'a.txt'
arq2 = 'b.txt'

hash1 = hashlib.new('ripemd160')

#update ira comparar strings
hash1.update(open(arq1, 'rb').read())
hash2 = hashlib.new('ripemd160')

hash2.update(open(arq2, 'rb').read())

#funcao digest resume os dados passados para o metodo update
print(hash1.digest() == hash2.digest())
#verifica se um arquivo tem o mesmo conteúdo do outro

#mostra o hash de cada arquivo

print(hash1.hexdigest())
print(hash2.hexdigest())


