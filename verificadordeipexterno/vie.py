import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url)
#passando dados que vem em formato json para dicionario
dados = json.load(resposta)
ip = dados['ip']
org = dados['org']
cid = dados['city']
pais = dados['country']
regiao = dados['region']
loc = dados['loc']

print('detalhes do seu ip externo')
print('ip: {4}\nRegiao: {1}\nPaís: {2}\nCidade: {3}\nOrg.:{0} '.format(org, regiao, pais,cid, ip))


print(dados)