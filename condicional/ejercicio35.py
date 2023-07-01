# Ejercicio de Condicional
#Comparar 2 edades e identificar que edad es mayor, menor o igual con respecto a los datos
# Edad de Pedro y otra edad de Pablo

edaddePedro = 70
edaddePablo = 50

print('Escriba la edad de Pedro')
edaddePedro=int(input())

print('Escriba la edad de Pablo')
edaddePablo=int(input())

if edaddePedro > edaddePablo:
    print('La edad de Pedro es Mayor que la de Pablo') 
elif edaddePedro == edaddePablo:
    print('La edad de Pedro es Igual a la Edad de Pablo')
else:
        print('La edad de Pablo es menor que la edad de Pedro')
