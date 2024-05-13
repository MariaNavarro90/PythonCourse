mi_lista = ['a','b','c']
print(type(mi_lista))

mi_lista = ['a','b','c']
print(len(mi_lista))

mi_lista = ['a','b','c']
resultado = mi_lista[0]
print(resultado)

mi_lista = ['a','b','c']
resultado = mi_lista[0:2]
print(resultado)

mi_lista = ['a','b','c']
mi_lista2 = ['d','e','f']
print(mi_lista + mi_lista2)

mi_lista = ['a','b','c']
mi_lista2 = ['d','e','f']
mi_lista3 = mi_lista + mi_lista2
print(mi_lista3)

#sobre escribir listas

mi_lista = ['a','b','c']
mi_lista2 = ['d','e','f']
mi_lista3 = mi_lista + mi_lista2

mi_lista3[0] = 'alfa'

print(mi_lista3)

#Metodos para las listas

mi_lista = ['a','b','c']
mi_lista2 = ['d','e','f']
mi_lista3 = mi_lista + mi_lista2

#agregar a la lista con .append
mi_lista3.append('g')
#remover un elemento de la lista con .pop
mi_lista3.pop() #al dejar vacio el parametro, va a tomar para eliminnar el ultimo elemento
#si lo quiero almacenar al elemento eliminado, lo puedo guardar en una variable
eliminado = mi_lista3.pop(0)
print(mi_lista3)
print( eliminado)

#ordenar las listas .sort
lista = ['a','d','s','f','j','z']
lista.sort()
lista.reverse()
print(lista)





