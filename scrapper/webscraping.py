from bs4 import BeautifulSoup
import requests

#objeto do site recebe o conteudo da requisição http do site
site = requests.get('https://www.climatempo.com.br/').content

#objeto soup baixa do site o html
soup = BeautifulSoup(site, 'html.parser')

#print(soup.prettify())
temperatura = soup.find('span' ,'class="_block _margin-b-5 -gray"')

print(temperatura.string)
