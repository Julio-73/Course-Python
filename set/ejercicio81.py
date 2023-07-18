# crear una aplicacion de de lista de Datos

print('escribe el numero aleatorio requerido')
cantidaddeNumero = input()

# variables

numeroVariable = 1
listaNumeros = []
# ciclo

while numeroVariable <= int(cantidaddeNumero):
    print('el siguiente numero '+ str(numeroVariable)+ ':')
    
    nuevoNumero=input()
    listaNumeros.append(int(nuevoNumero))
    numeroVariable += 1
   
    print('Numero total de lista',listaNumeros)