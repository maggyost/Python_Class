''' Programa:Ciencia de Datos con Python
    Modulo 01:   Fundamentos de Python
    Sesion 01:  Tipos de Objetos
    Fecha:      21/07/2019
    Version:    1
    Author:     Magaly Ostos'''
'''
#Enteros
print(10)
#Decimales
print(3.1415)
#Texto
print("mes de julio")
'''
'''
nro= 10
pi=3.1415
msg="Mes de Julio"
print(nro)
print(pi)
print(msg)

#Tipo de Objeto
print(type(nro))
print(type(pi))
print(type(msg))
'''
'''
nro= -1
print(type(nro))
nro= 3.1415
print(type(nro))
nro= "Mes de Julio"
print(type(nro))
nro= 0
print(type(nro))
'''
#Son funciones int() float() str()
'''
print(int(3.7415))
print(float(1))
print(int("3"))
print(float("12")) # Se convierte float
#print(int("12.45")) # Este Falla porq en int no hay punto .
print(float("12.45"))
print(str("12.45"))#Esto es cadena
print(str("-1")) #Esto es cadena
'''
'''Para Booleano'''

a = True
print(type(a))

b = "True"
print(bool(b))

print(not (a) )