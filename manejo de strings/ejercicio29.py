# Format
# Ejemplo 1
cantidad= 3
numeroID= 10
precio=59.90

PrecioDeVenta= 'El producto vale {} y son {} productos el numero de control es {}'

print(PrecioDeVenta.format(precio,cantidad,numeroID))


# Ejemplo 2

a= 'usuario'
b= 'producto'
c= 'marca'
d=' cantidad'
e= 200

resultadodeVenta = 'El {} conpro el {} de la {} y la {} Nike a un precio de {} soles. '

print(resultadodeVenta.format(a,b,c,d,e ))


