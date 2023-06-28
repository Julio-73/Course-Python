# Operadores Aritméticos 

print('Dame un Valor numerico')
a= int(input())

print('Dame un Segundo Valor')
b= int (input())

#Ejemplo de una Suma
suma = a+b
# Ejemplo de una Resta
resta= a-b
# Ejemplo de una Multiplicación
multiplicación =a*b
# Ejemplo de una División
división =a/b
#Exponente
exponente = a**b
#floor
floor = a//a
# Modulo
modulo= a%b # --> es el residuo



print(suma)
print(resta)
print(multiplicación)
print(división)
print(exponente)
print(floor)
print(modulo)


# Ejemplo 2 


print('Valor Numerico')
x = int(input())

print('Segundo valor Numerico')
y = int(input())

print('Tercer valor Numerico')
k = int(input())

print('Cuarto valor Numerico')
t = int(input())

operar1 = x + y + k + t
operar2 = x - y - k - t
operar3 = x * y * k * t
operar4 = x / y / k / t
operar5 = x ** y ** k ** t
operar6 = x // y // k // t
operar7 = x % y % k % t

print(operar1)
print(operar2)
print(operar3)
print(operar4)
print(operar5)
print(operar6)
print(operar7)

# Ejemplo 3

print('tres numeros aleatorios')
a,b,c = int(input()), int(input()), int(input())

respuesta = a * b + c
print('Respuesta de la operación: --->', respuesta)
