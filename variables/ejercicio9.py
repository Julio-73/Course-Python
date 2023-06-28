""" Solicitar valores para operación simple
"""

# Ejemplo 1

print('Dame un Primer Valor')
valor1=input()

print('Dame un segundo Valor')
valor2=input()

valor3 = int(valor1) + int (valor2)
print('El resultado de las dos Variables es: ', valor3)


#Ejemplo 2

print('Dame un numero')
a=input()

print('Dame un segundo Numero')
b=input()

print('Dame un tercer Numero')
c=input()

d = int(a)+ int(b)+ int(c)

print('El resultado de las tres Variables es:', d)



# Ejemplo 3

print('dame una oracion de texto')
text=input()

print('dame una segunda oracion de texto')
text2=input()

print('dame una tercera oracion de texto')
text3=input()

text4 = str(text)+ str(text2)+ str(text3)
print('La cadena de texto es:', text4)