
casas = {'calle': 20, 'numero': 30, 'año de creación': 1900, 'país': 'méxico'}

casas.pop('calle') # pop  elimina un string
print(casas)

casas.update({'calle': 20})
print(casas) # update egrga el string

print(casas.get('numero')) # get verifica el indice

casas.clear() # clear elimina todo
print(casas)
