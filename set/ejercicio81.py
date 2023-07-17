
# crear una Aplicación
# le solicite al usuario una cantidad de numeros a ingresar a una lista
# Posteriormente imprimir dicha lista

print('escriba la cantidad de numero requerido ----__----')
cantidaddeNumeros = input()


Numeros = 1
listadeNumeros = []

# ciclo

while Numeros <= int(cantidaddeNumeros):
    print('el siguiente numero es ---> '+ str(cantidaddeNumeros))
    
    nuevoNumero= input()
    listadeNumeros.append(int(nuevoNumero))
    Numeros += 1
    
    print('Total numeros en esta lista es ---->' + str(listadeNumeros))
    
