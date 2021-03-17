numeroarvo = '123.45'
pilkunpaikka = numeroarvo.find('.')
print(pilkunpaikka)
osat = numeroarvo.split('.')
print(osat, 'osia on', len(osat), 'kpl')
print(osat.isnumeric())