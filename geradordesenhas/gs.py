import random, string

tamanho = int(input('Digite o tamanho da senha: '))

chars = string.ascii_letters + string.digits + string.punctuation


rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))