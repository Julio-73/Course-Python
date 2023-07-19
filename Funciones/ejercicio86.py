# funciones de Argumentos variables

def algoritmo(*valores): # puedes pomner todos los valores que tu desees
    a=valores[0]
    b=valores[1]
    c=valores[2]
    d = a+b-c 
    return('el resultado de la operación es -->'+ str(d))
    
print(algoritmo(10,20,400))   