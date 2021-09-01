from threading import Thread
import time


def carro1(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        print(f'carro: {trajeto} {piloto}')

        print('\n')
        trajeto += velocidade
        time.sleep(0.5)



#target é a função e os args sao ssados em lista
t_carro1 = Thread(target=carro1, args=[1, 'Seila'])

t_carro2 = Thread(target=carro1, args=[2, 'wopam'])

print('comecou 1')
t_carro1.start()
print('comecou 2')
t_carro2.start()