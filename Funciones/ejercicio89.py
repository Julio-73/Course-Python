
# Hacer una aplicacion para calcular el  imc
# y mostrarle al usuario su peso indicando,si tiene peso bajo,normal u obecidad

# IMC = peso/(estatura*estatura)
# Imc <18.5 (peso bajo), imc 18.5> y<29.9(normal),imc >29.9(obesidad)

# Imprimir variables

def calcularIMC(peso,estatura):
    IMC=peso/(estatura*estatura)
    if IMC <18.5:
        print('peso bajo')
    else :
        if IMC >18.5 and IMC <29.9:
            print('peso normal')
        else:
            if IMC >29.9:
                print('obecidad')
                
print('escribe tu nombre:')    
nombre=input()            

print('escribe tu peso:')
peso=int(input())

print('escribe tu estatura:')
estatura=float(input())
                
print('esto es su peso --__-- ')                
calcularIMC( peso,estatura )               
    