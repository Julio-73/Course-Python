# tuplas

user = ['chan', 'jacky', 'tom', 'teller']
print(user)

print(user[3])
total = tuple(user)  # convertir a tuplas --_-- tuple

print(total)
total = list(user)  # convertir a listado --_-- list
print(total)

user.append('tiesto')
print(user)

user.insert(2, 'davis')  # insert agrega un string specifico --_--
print(user)

user.pop(0)  # pop elimina un indice specifico --_--
print(user)

user.remove('teller')
print(user)  # remove elimina un string specifico --_--

del user[3]  # del elimina un string specifico --_--
print(user)

print(user.index('davis'))  # index busca el indice specifico --_--

print(type(user))  # class str --_--



