from phonenumbers import geocoder
from phonenumbers import carrier
import phonenumbers


telefone = input('Digite o telefone no formato +551140028922:')

phone_number = phonenumbers.parse(telefone)

print(geocoder.description_for_number(phone_number, 'pt'))
print(carrier.name_for_number(phone_number, 'pt'))



