import os

ip_ou_host = input('Digite o Ip ou Host a ser verificado: ')

os.system(f'ping {ip_ou_host}')