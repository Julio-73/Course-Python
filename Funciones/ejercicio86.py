# funciones de Argumentos variables

def algoritmo(*valores): # puedes pomner todos los valores que tu desees
    a=valores[0]
    b=valores[1]
    c=valores[2]
    d = a+b-c 
    return('el resultado de la operación es -->'+ str(d))
    
print(algoritmo(10,20,400))   



# ejemplo 2


def valor(*valores):
    a = valores[0]
    b = valores[1]
    c = valores[2]
    d = valores[3]
    z = a+b+c/d
    print('el resultado de la función es:---> ' + str(z) + ':')


valor(12, 40, 50, 20)

# ejemplo 3


def operar_1(a, b, c):

    while (a == 10 and b != 20 or c == 2):
        return ('esto es una operacion logica ---> ' + str(a*b-c))
    else:
        return ('Esto no es una operacion logica---> Entiendes o No ?')


result = operar_1(10, 10, 2)
print(result)

# ejemplo 4


def ecuacion_1(x, z):
    while (x >= 20 and z <= 10):
        z = x+z+(200-40*2)
        return ('esto es una ecuacion paralela ---> '+str(z))
    else:
        return ('esta ecuación esta mal planteada me entienedes o te explico  ')
    
print(ecuacion_1(30, 0))


